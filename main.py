#!/usr/bin/env python3

import sys
import subprocess

if __name__ == '__main__':
    PYTHON3 = sys.executable
    cliargs = [PYTHON3, 'sub.py']
    print("Before call", file=sys.stderr)
    rv = subprocess.check_output(cliargs)
    print("After call", file=sys.stderr)
    print("Summary")
    print("1")
    print("2")
    print("3")
