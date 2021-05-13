#!/usr/bin/env python3

import subprocess
import sys

_cmd = 'ping -c4 1.1.1.1'
_cmd_timeout = 5

send_ping = subprocess.Popen(
    _cmd, 
    stdout=subprocess.PIPE, 
    shell=True, 
    universal_newlines=True
)

try:
    (output, error) = send_ping.communicate(timeout=_cmd_timeout)
except subprocess.TimeoutExpired:
    print(f"Command execution timeout: '{_cmd}'")
    send_ping.terminate()
else:
    print(f"[-] Command return code: {send_ping.returncode}")
    print(f"[-] Command output data type: {type(output)}")

    ### ---universal_newlines=True--- ###
    print(f"[-] Command output:\n{output}")                     
    
    ### ---universal_newlines=False (default)--- ###
    # print(f"[-] Command output:\n{output.decode('utf-8')}")


### ---NO argument--- ###
# ret_code = subprocess.call('date')

### ---WITH argument--- ###
# ret_code = subprocess.call(['ls', '-al', '/etc/os-release'])