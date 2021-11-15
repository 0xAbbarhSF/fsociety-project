# hash cracker for md5, sha512, sha256, ntlm
import hashlib
import binascii
import time
import sys

try:
	passwrd = sys.argv[2]
	lst = sys.argv[3]
	verify = []
	def md5():
		print("[*] cracking started with md5 alogrithm")
		start = time.perf_counter()
		with open(lst, 'r', encoding='latin1') as l:
			passwds = l.readlines()
			print(f"[+] trying with {len(passwds)} passwords")
			for passwd in passwds:
				password = passwd.strip()
				hashed_object = hashlib.md5(password.encode())
				hashed_password = hashed_object.hexdigest()
				if hashed_password == passwrd:
					verify.append(1)
					finish = time.perf_counter()
					print(f"[*] password cracked: {password}")
					print(f"[+] finished in {round(finish-start, 2)} second(s)")
					exit()


	def sha512():
		print("[*] cracking started with sha512 alogrithm")
		start = time.perf_counter()
		with open(lst, 'r', encoding='latin1') as l:
			passwds = l.readlines()
			print(f"[+] trying with {len(passwds)} passwords")
			for passwd in passwds:
				password = passwd.strip()
				hashed_object = hashlib.sha512(password.encode())
				hashed_password = hashed_object.hexdigest()
				if hashed_password == passwrd:
					verify.append(1)
					print(f"[*] password cracked: {password}")
					finish = time.perf_counter()
					print(f"[+] finished in {round(finish-start, 2)} second(s)")
					exit()


	def sha256():
		print("[*] cracking started with sha256 alogrithm")
		start = time.perf_counter()
		with open(lst, 'r', encoding='latin1') as l:
			passwds = l.readlines()
			print(f"[+] trying with {len(passwds)} passwords")
			for passwd in passwds:
				password = passwd.strip()
				hashed_object = hashlib.sha256(password.encode())
				hashed_password = hashed_object.hexdigest()
				if hashed_password == passwrd:
					verify.append(1)
					print(f"[*] password cracked: {password}")
					finish = time.perf_counter()
					print(f"[+] finished in {round(finish-start, 2)} second(s)")
					exit()



	def ntlm():
		print("[*] cracking started with ntlm alogrithm")
		start = time.perf_counter()
		with open(lst, 'r', encoding='latin1') as l:
			passwords = l.readlines()
			print(f"[+] trying with {len(passwords)} passwords")
			for password in passwords:
				passwd = password.strip()
				hashedList = hashlib.new('md4', passwd.encode('utf-16le')).digest()
				ntlmHash = binascii.hexlify(hashedList).decode()
				if ntlmHash == passwrd:
					verify.append(1)
					print(f"[*] password cracked: {passwd}")
					finish = time.perf_counter()
					print(f"[+] finished in {round(finish-start, 2)} second(s)")
					exit()


	if sys.argv[1] == "md5":
		md5()
	if sys.argv[1] == "sha256":
		sha256()
	if sys.argv[1] == "sha512":
		sha512()
	if sys.argv[1] == "ntlm":
		ntlm()
	if not verify:
		print("[-] password did not found !")

except IndexError:
	print("[!] usage: python3 HASHTYPE HASH LIST\n[+] available algorithms: md5 sha512 sha256 ntlm")

except KeyboardInterrupt:
	print("\n[-] exited")
