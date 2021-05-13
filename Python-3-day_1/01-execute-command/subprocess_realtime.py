#!/usr/bin/env python3

import sys
import subprocess

_ping_count = 4
_cmd = "ping -c{} 1.1.1.1".format(_ping_count)

send_ping = subprocess.Popen(
    _cmd, 
    shell=True, 
    stderr=subprocess.PIPE, 
    universal_newlines=True
)

while send_ping.poll() is None:
    send_ping.stderr.read(1)            #send to interpreter stdout
    #out = send_ping.stdout.readline()  #stored in variable out