#!/usr/bin/python3
# simple utility for domain validation
import requests
import sys
try:
	valid_domains = []
	redirects = []
	with open(sys.argv[1], 'r', encoding='latin1') as d:
		domains = d.readlines()
		print(f"[+] trying with {len(domains)} domain(s) ")
		print("[+] this may take a while")
		print("\t")
		for dom in domains:
			domain = dom.strip()
			try:
				url = f"https://{domain}"
				r = requests.get(url, verify=True, allow_redirects=False)
				if  r.status_code == 302 or r.status_code == 200:
					valid_domains.append(domain)
				if r.status_code == 403:
					print(f"[+] forbidden domain: {domain}")
				if r.status_code == 301:
					valid_domains.append(domain)
					redirects.append(domain)
			except requests.exceptions.ConnectionError:
				pass
	if valid_domains:
		print(f"[*] found {len(set(valid_domains))} valid domains:")
		for valid_domain in set(valid_domains):
			print(f"[*] {''.join(valid_domain)}")


	if redirects:
		print("\t")
		print("[+] detecting location of the redirection domains")
		print("\t")
		for d in set(redirects):
			r = requests.get(f'https://{d}/', verify=True, allow_redirects=False)
			print(f"[*] {d} redirected to ===> {r.headers['Location']}")	
			
except IndexError:
	print("usage: python3 domain_checker.py DOMAIN_LIST.txt")
except KeyboardInterrupt:
	print("\n[-] exited")
