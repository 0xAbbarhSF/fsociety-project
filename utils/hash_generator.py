import hashlib
import sys
import binascii


try:
	password = sys.argv[2]


	def md5():
		hashed_password = hashlib.md5(password.encode())
		hashed_password0 = hashed_password.hexdigest()

		print(hashed_password0)


	def sha512():
		hashed_password = hashlib.sha512(password.encode())
		hashed_password0 = hashed_password.hexdigest()

		print(hashed_password0)


	def sha256():
		hashed_password = hashlib.sha256(password.encode())
		hashed_password0 = hashed_password.hexdigest()

		print(hashed_password0)


	def ntlm():
		hashed_password = hashlib.new('md4', password.encode('utf-16le')).digest()
		hashed_password0 = binascii.hexlify(hashed_password).decode()

		print(hashed_password0)



	if sys.argv[1] == "md5":
		md5()

	if sys.argv[1] == "sha256":
		sha256()

	if sys.argv[1] == "sha512":
		sha512()

	if sys.argv[1] == "ntlm":
		ntlm()


except IndexError:
	print("[!] usage: python3 hash_generator.py HASHTYPE STRING \n[+] available algorithms: md5 sha512 sha256 ntlm")