#!/usr/bin/env python
import subprocess
import sys

interface = sys.argv[1]
mac_address = sys.argv[2]

print(f"[+] Changing MAC address for {interface} to {mac_address}")
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
subprocess.call(["ifconfig", interface, "up"])
