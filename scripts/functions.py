#!/usr/bin/env python3

import json
import socket
from subprocess import getoutput


def load_list(filename):
    ip_list = {}
    with open(filename) as file:
        for line in file.readlines():
            node = line.rstrip().split(",")
            ip_list[node[0]] = [node[1], node[2], node[3], node[4]]
    return ip_list


def get_height_info(ip, is_rust=True):
    path = "cpp" if not is_rust else "rust"
    call = f"ssh root@{ip} 'bash -s' < $(pwd)/commands/{path}/get_height.sh"

    results = getoutput(call).rstrip()
    return int(results)


def get_connected_peers_info(ip, is_rust=True):
    inbounds = 0
    outbounds = 0
    path = "cpp" if not is_rust else "rust"
    call = f"ssh root@{ip} 'bash -s' < $(pwd)/commands/{path}/get_connected_peers.sh"

    results = getoutput(call).rstrip()
    connected_peers = json.loads(results)
    for peer in connected_peers:
        if peer["direction"] == "Outbound":
            outbounds += 1
        else:
            inbounds += 1
    return inbounds, outbounds


def check_port(ip, port=3414):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    is_open = result == 0
    sock.close()
    return is_open
