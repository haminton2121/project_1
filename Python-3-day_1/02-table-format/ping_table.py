#!/usr/bin/env python3

"""
rich requires Python 3.6.1 and above
"""

import subprocess
import sys
import rich
from rich import box
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.tree import Tree


_ping_count = 4
_ping_host  = '1.1.1.1'
_cmd = "ping -c{} {}".format(_ping_count, _ping_host)

send_ping = subprocess.Popen(
    _cmd, 
    shell=True, 
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    universal_newlines=True
)

table = Table(
    "ICMP Seq",
    "TTL",
    "Time",
    box=box.SIMPLE
)

rich.print(Panel(
    "Host: [red]{}[/red]".format(_ping_host) + "\n" +
    "Packets: [blue]{}[/blue]".format(_ping_count),     
    title="Simple ping ultility",
    expand=False)
)

with Live(table, refresh_per_second=4):
    while send_ping.poll() is None:
        out = send_ping.stdout.readline()
        
        if "from 1.1.1.1:" in out.strip():
            arr = out.split()
            table.add_row(arr[4].split('=')[1], arr[5].split('=')[1], arr[6].split('=')[1])