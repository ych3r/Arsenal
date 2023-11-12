# MAC address changer

Why would you want to change the MAC address?

- MAC Spoofing

---

Check network info: `ifconfig`

Disable eth0: `ifconfig eth0 down`

Change MAC address: `ifconfig eth0 hw ether 00:11:22:33:44:55`

Enable eth0: `ifconfig eth0 up`

Original MAC address: `ethtool -P eth0`

---

```sh
Usage: mac_changer.py [options]

Options:
  -h, --help            show this help message and exit
  -i INTERFACE, --interface=INTERFACE
                        Interface to change its MAC address
  -m MAC_ADDRESS, --mac=MAC_ADDRESS
                        New MAC address
```