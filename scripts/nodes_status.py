#!/usr/bin/env python3

import os
from time import sleep

from functions import add_rows_to_table, create_table, load_list

SLEEP_SECONDS = 0
FILENAME = "iplist.txt"
clear = lambda: os.system("tput reset")


if __name__ == "__main__":
    while True:
        nodes = load_list(FILENAME)
        table = add_rows_to_table(create_table(), nodes)
        clear()
        print(table, flush=True)
        sleep(SLEEP_SECONDS)
