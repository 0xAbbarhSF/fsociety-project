#!/usr/bin/python3
# simple email harvesting utility using hunter.io api key
import requests
import sys
import re

try:

	api_key = "b6f7d9fdf7e54971b39a551c5635b360469bddd1"

	domain = sys.argv[1]

	api_query = f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={api_key}"

	r = requests.get(api_query)

	pattern = re.compile(r'(value)(.*)', re.I)

	emails = pattern.findall(r.text)

	if emails:

		print("[*] found emails:")
		print("\t")
		for e in emails:
			global email
			emails = ''.join(e).replace("value", "")
			e2 = emails.strip('"')
			e3 = e2.replace('"', '')
			e4 = e3.replace(":", '')
			e5 = e4.replace(",", '')
			email = e5.replace(" ", '')
			print(f"[*] {email}")
	else:
		print("[-] did not find any emails")

except IndexError:
	print("[-] usage: python3 email_finder.py something.com")