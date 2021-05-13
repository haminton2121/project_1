#!/usr/bin/env python3
# link: https://stackoverflow.com/questions/3503879/assign-output-of-os-system-to-a-variable-and-prevent-it-from-being-displayed-on

from os import system, remove
from uuid import uuid4

def bash_(shell_command: str) -> tuple:

    logfile: str = '/tmp/%s' % uuid4().hex
    err: int = system('%s &> %s' % (shell_command, logfile))
    out: str = open(logfile, 'r').read()
    remove(logfile)
    return err, out

ret_code, ret_text = bash_('cat /etc/*release')

print(f"Status code: {ret_code}")
print(f"Output: {ret_text}")

