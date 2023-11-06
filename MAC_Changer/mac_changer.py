#!/usr/bin/env python3
import subprocess
import sys

interface = sys.argv[1]
mac_address = sys.argv[2]

subprocess.call(f"ifconfig {interface} down", shell=True)
subprocess.call(f"ifconfig {interface} hw ether {mac_address}", shell=True)
subprocess.call(f"ifconfig {interface} up", shell=True)
subprocess.call(f"ifconfig {interface}", shell=True)