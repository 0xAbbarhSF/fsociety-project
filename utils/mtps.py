#!/usr/bin/python3

# Multi Threaded Port Scanner
import socket
import time
import sys
import os
import argparse
from concurrent.futures import ThreadPoolExecutor

parser = argparse.ArgumentParser(epilog='(M)ulti (T)hreaded (P)ort (S)anner')
parser.add_argument('--target', '-t', help='target ip address', required=True)
parser.add_argument('--threads',type=int, default=3000, help='number of threads to work with (default: 3000)')
parser.add_argument('--no_nmap', action='store_true', help='scan without running nmap on the open ports')


args = parser.parse_args()
target = args.target


nmap_list = []

print('[*] Multi Threaded Port Scanner')
if os.getuid() == 0:

	print(f'[*] setting the file limit to: {args.threads * 2}')
	os.system(f'ulimit -n {args.threads * 2}')
print("[+] starting port scanning")

print("\t")
start = time.perf_counter()
	
def connect(targetIP, port):
	

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
		sock.settimeout(0.5)
		# if port == 65354:

		# 	print(f'[*] reached the last port: {port}')
		if sock.connect((targetIP, port)) == None:
			print(f"[*] {targetIP}:{port} is open ")
			nmap_list.append(port)


with ThreadPoolExecutor(args.threads) as ex:	

	result = [ex.submit(connect, target, port) for port in range(1, 65355)]


finish = time.perf_counter()
print(f"[+] finished in {round(finish-start, 2)} second(s)")


def nmap_scan():

	string = str(nmap_list)
	nmap_p = ''.join(string.strip('[]')) # ---> NMAP PREPS
	nmap_ports = nmap_p.replace(' ','')


	print('\t')
	print("[*] starting full nmap scan on the open ports")
	print("---------------------------------------------")
	time.sleep(1.5)
	print(f"[+] command will be used: nmap -sV -sC -p {nmap_ports} -T4 --min-rate=10000 -A -O -oN nmap_detailed {target} ")
	print("\t")
	os.system(f"nmap -sV -sC -p {nmap_ports} -T4 --min-rate=10000 -A -O -oN nmap_detailed {target} ")

	print("\t")
	print("[*] the scan results saved in [nmap_detailed] file")


if not args.no_nmap:

	nmap_scan()













# for port in range(65300):


	# connect(target, port)
# string = str(nmap_list)
# nmap_p = ''.join(string.strip('[]')) # ---> NMAP PREPS
# nmap_ports = nmap_p.replace(' ','')

# print(nmap_ports)