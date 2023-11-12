# Network Scanner

ARP Scanner using Scapy library.

## Set up lab environment (Virtualbox)

Two vm will not be able to talk to each other in NAT mode, you must set up a NAT network.

Go to `File -> Tools -> Network Manager`

Create a NAT network under `NAT Networks`

Go to each vm, `Settings -> Network -> Adapter 1 -> NAT Network`

Then, they can find each other in the network.

---

```sh
usage: network_scanner.py [-h] [-t TARGET]

options:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target range to scan
```