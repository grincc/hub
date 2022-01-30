#!/usr/bin/env python3

import argparse
import hashlib
import os
import shutil
import signal
import subprocess
import sys
from pathlib import Path
from subprocess import check_output

import requests


def get_latest_release(prelease=False):
    filename = ""
    download_url = ""
    tags = requests.get(
        "https://api.github.com/repos/GrinPlusPlus/GrinPlusPlus/tags"
    ).json()
    for tag in tags:
        if download_url:
            break
        name = tag["name"]
        release = None
        if not prelease and "beta" in name:
            continue
        print(f"\tGetting assets for {name}...")
        release = requests.get(
            f"https://api.github.com/repos/GrinPlusPlus/GrinPlusPlus/releases/tags/{name}"
        ).json()
        for asset in release["assets"]:
            if asset["name"].endswith(".AppImage"):
                filename = asset["name"]
                download_url = asset["browser_download_url"]
                break
    return filename, download_url


def download_release(download_url, filename):
    open(filename, "wb+").write(requests.get(download_url, allow_redirects=True).content)
    os.chmod(filename, 0o755)


def extract_appimage_file(filename):
    filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)
    subprocess.check_output(
        [
            filepath,
            "--appimage-extract",
        ]
    )


def stop_grin_node():
    try:
        requests.get("http://127.0.0.1:3413/v1/shutdown")
    except:
        pass
    try:
        pid = check_output(["pidof", args.binary])
        os.kill(int(pid), signal.SIGKILL)
    except:
        pass


def clean_peers_folder():
    try:
        folder = f"{Path.home()}/.GrinPP/MAINNET/NODE/DB/PEERS"
        for file_found in os.listdir(folder):
            file_path = os.path.join(folder, file_found)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except:
                pass
    except:
        pass


def copy_node_to_destination(destination):
    shutil.copy2(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "squashfs-root/resources/app.asar.unpacked/bin/GrinNode",
        ),
        destination,
    )  # preserve file metadata.
    return hashlib.md5(open(destination, "rb").read()).hexdigest()


def copy_tor_to_destination(destination):
    shutil.copytree(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "squashfs-root/resources/app.asar.unpacked/bin/tor",
        ),
        f"{destination}/tor",
        dirs_exist_ok=True,
    )  # preserve file metadata.


def remove_files(appimage_file):
    shutil.rmtree(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "squashfs-root",
        )
    )

    os.unlink(
        os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            appimage_file,
        )
    )


def add_permissions(destination, binary):
    os.chmod(f"{destination}/{binary}", 0o755)
    os.chmod(f"{destination}/tor/tor", 0o755)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Grin++ Downloader")
    parser.add_argument(
        "--prelease",
        dest="prelease",
        action="store_true",
        help="Download prelease if the prelease is the latest release (default: false)",
    )
    parser.set_defaults(prelease=False)
    required = parser.add_argument_group("required named arguments")
    required.add_argument("-d", "--destination", help="Destination folder", required=True)
    required.add_argument("-b", "--binary", help="Name of the binary", required=True)

    args = parser.parse_args()

    p = Path(args.destination)

    if not p.exists() or not p.is_dir():
        print("ERROR: Invalid destination folder.")
        sys.exit(1)
    if not os.access(args.destination, os.W_OK):
        print("ERROR: Destination folder is not writable.")
        sys.exit(1)

    print("Getting the latest release...")
    filename, download_url = get_latest_release(args.prelease)

    if not download_url:
        print("ERROR: Can't get download URL.")
        sys.exit(1)

    print(f"Downloading {filename} file...")
    download_release(download_url, filename)

    print("Extracting Grin node...")
    extract_appimage_file(filename)

    print("Stopping Grin node...")
    stop_grin_node()

    print("Cleaning up peers database...")
    clean_peers_folder()

    print("Copying GrinNode binary...")
    hexdigest = copy_node_to_destination(f"{args.destination}/{args.binary}")

    print("Copying tor folder...")
    copy_tor_to_destination(args.destination)

    print("Assigning execution permissions...")
    add_permissions(args.destination, args.binary)

    print("Removing unnecesary files...")
    remove_files(filename)

    print("Done.")

    binary_path = os.path.join(args.destination, args.binary)
    binary_checksum = hashlib.md5(open(binary_path, "rb").read()).hexdigest()

    if hexdigest == binary_checksum:
        print("\nTip: Start Grin node in brackground by executing the next command:")
        print(f"\t\tnohup {binary_path} > /dev/null 2>&1 &\n")
    else:
        print("\n\tERROR: checksums are not the same!")
        print(f"\t\t{hexdigest} != {binary_checksum}\n")
