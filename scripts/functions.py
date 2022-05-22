#!/usr/bin/env python3

import json
import socket
from datetime import datetime
from subprocess import getoutput

from prettytable.colortable import ColorTable, Themes


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


def create_table():
    table = ColorTable(theme=Themes.OCEAN)
    table.field_names = [
        "",
        "IP",
        "Height",
        "Inbounds",
        "Outbounds",
        "Agent",
        "City",
        "State",
        "Date",
        "Time",
        "Network",
    ]
    return table


def add_rows_to_table(table, nodes):
    i = 1
    for ip in nodes:
        node_info = nodes[ip]
        updated_at = datetime.now()
        is_rust = "Grin++" not in node_info[0]
        height = get_height_info(ip, is_rust)
        inbounds, outbounds = get_connected_peers_info(ip, is_rust)
        table.add_row(
            [
                i,
                ip,
                height,
                inbounds,
                outbounds,
                node_info[0],
                node_info[1],
                node_info[2],
                updated_at.strftime("%d-%b-%Y"),
                updated_at.strftime("%H:%M:%S"),
                node_info[3],
            ]
        )
        i += 1


def check_port(ip, port=3414):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    is_open = result == 0
    sock.close()
    return is_open
