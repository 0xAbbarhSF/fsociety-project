import requests
import json
import sys

try:

	ipv4 = sys.argv[1]

	r = requests.get(f"http://ipinfo.io/{ipv4}/json")

	r1 = requests.get(f"http://ip-api.com/json/{ipv4}") 

	info = json.loads(r.text)
	info1 = json.loads(r1.text)

	print(f"[+] pulling down information for {info['ip']}")
	print("\t")
	print(f"[*] country: {info1['country']}")
	print(f"[*] country code: {info1['countryCode']}")
	print(f"[*] city: {info['city']}")
	print(f"[*] coordinates: {info['loc']}")
	print(f"[*] ISP: {info['org']}")
	print(f"[*] used time zone {info['timezone']}")
except IndexError:
	print("[!] usage: python3 IPV4")