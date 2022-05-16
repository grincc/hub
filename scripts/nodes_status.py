#!/usr/bin/env python3

import os
from datetime import datetime
from time import sleep

from prettytable.colortable import ColorTable, Themes

from functions import load_list, get_height_info, get_connected_peers_info

SLEEP_SECONDS = 0
FILENAME = "iplist.txt"
clear = lambda: os.system("tput reset")

if __name__ == "__main__":
    while True:
        nodes = load_list(FILENAME)
        x = ColorTable(theme=Themes.OCEAN)
        x.field_names = [
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
        i = 1
        for ip in nodes:
            node_info = nodes[ip]
            updated_at = datetime.now()
            is_rust = "Grin++" not in node_info[0]
            height = get_height_info(ip, is_rust)
            inbounds, outbounds = get_connected_peers_info(ip, is_rust)
            x.add_row(
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
        clear()
        print(x, flush=True)
        sleep(SLEEP_SECONDS)
