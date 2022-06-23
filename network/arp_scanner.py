# simple arp scanner to identify devices on the network that doesn't respond to ping

import scapy.all as scapy 
from mac_vendor_lookup import MacLookup
import click

def arp(target):
	print(f"scanning {target}\n")
	ipv6_list = []
	
	arp_p = scapy.ARP(pdst=target)
	broadcast_p = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_broadcast_p = broadcast_p/arp_p
	element_list = scapy.srp(arp_broadcast_p, timeout=1, verbose=False)[0]

	discoverd = []

	def mac_lookup(mac):
		for mac in ipv6_list:
			try:

				vendor = MacLookup().lookup(mac)
			except Exception as e:
				pass
		return vendor	



	for element in  element_list:

		ipv6_list.append(element[1].hwsrc)
		discoverd_dict = {
			"IP": element[1].psrc,
			"MAC": element[1].hwsrc,
			"vendor": mac_lookup(element[1].hwsrc),
		}

		discoverd.append(discoverd_dict)

	print("[*] discoverd devices:\n")
	print("   ipv4\t\t\tipv6\t\t\tvendor")
	print("   ")
	for i in discoverd:
		print(i["IP"],'\t', i["MAC"], '\t', i["vendor"])



def arp_spoofed(target,spoofed):
	print(f"scanning {target}\n")
	
	ipv6_list = []
		
	arp_p = scapy.ARP(pdst=target, psrc=spoofed)
	broadcast_p = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_broadcast_p = broadcast_p/arp_p
	element_list = scapy.srp(arp_broadcast_p, timeout=1, verbose=False)[0]

	discoverd = []

	def mac_lookup(mac):
		for mac in ipv6_list:
			try:
				vendor = MacLookup().lookup(mac)
			except Exception as e:
				pass
		return vendor	



	for element in  element_list:

		ipv6_list.append(element[1].hwsrc)
		discoverd_dict = {
			"IP": element[1].psrc,
			"MAC": element[1].hwsrc,
			"vendor": mac_lookup(element[1].hwsrc),

		}


		discoverd.append(discoverd_dict)

	print("[*] discoverd devices:\n")
	print("   ipv4\t\t\tipv6\t\t\tvendor")
	print("   ")
	for i in discoverd:
		print(i["IP"],'\t', i["MAC"], '\t', i["vendor"])


@click.command()
@click.option('--target','-t', type=str, help='ipv4 range to scan ex:192.168.0.0/24')
@click.option('--spoof','-s',type=str,help='ipv4 to spoof the packets with')
def scan(target,spoof):
	
	if spoof:
		arp_spoofed(target,spoof)

	else:
		arp(target)






scan()
