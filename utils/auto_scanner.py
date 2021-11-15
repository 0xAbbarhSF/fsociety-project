#!/usr/bin/python3
# simple and and fast port scanner with nmap
import socket
import time
import sys
import os

try:
	
	nmap_list = []
	targetIP = sys.argv[1]

	
	print("[+] starting port scanning")
	print("\t")
	start = time.perf_counter()
	for port in range(65353):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.1)
		result = sock.connect_ex((targetIP, port))
		if result == 0:
			print(f"[*] {targetIP}:{port} is open ")
			nmap_list.append(port)

	
	string = str(nmap_list)
	nmap_p = ''.join(string.strip('[]'))
	nmap_ports = nmap_p.replace(' ','')
	print('\t')
	print("[*] starting full nmap scan on the open ports")
	print("---------------------------------------------")

	print(f"[+] command will be used: nmap -sV -sC -p {nmap_ports} -T4 -A -oN nmap_initial {targetIP} ")
	print("\t")
	os.system(f"nmap -sV -sC -p {nmap_ports} -T4 -A -oN nmap_initial {targetIP} ")
	finish = time.perf_counter()
	print("\t")
	print("[+] the scan results saved in [nmap_initial] file")
	print(f"[+] finished in {round(finish-start, 2)} second(s)")

except IndexError:
	print("[-] usage: python3 auto_scanner.py <IP> ")
	

except KeyboardInterrupt:
	print("\n[-] exited")