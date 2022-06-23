# uses multiple processors for executing parrellel tasks for performance improvments

from crypt import crypt
import sys
import re
from time import perf_counter
from concurrent.futures import ProcessPoolExecutor
import argparse
# from pwn import logging


parser = argparse.ArgumentParser()

parser.add_argument('--hash', required=True, help='crypt hash (algorithm determined automatically)')
parser.add_argument('--wordlist', '-w', required=True, help='password list')
parser.add_argument('--processors', '-p', type=int,required=True, default=1, help='how many processors to execute (default: 1)')
parser.add_argument('--verbose', '-v', action='store_true', help='verbose attempts')


args = parser.parse_args()

print(f'[*] using {args.processors} processors')
hashed_password = args.hash
password_lst = args.wordlist


def salt_extract(hashed): 
	
	pattern = re.compile(r'[$]\d[$].+\d*.+\w*.+[$]')

	match = pattern.findall(hashed)

	s = ''.join(match)

	salt = list(s)

	salt[19] = ''

	return ''.join(salt) 
	

def create_hash(password,salt):

	encrypted = crypt(password, salt)

	return encrypted


def hash_id(salt):
	if "$6$" in salt:
		print("[+] hash type: SHA-512crypt\n")

	if "$5$" in salt:
		print("[+] hash type: SHA-256crypt\n")

	if "$1$" in salt:
		print("[+] hash type: MD5crypt\n")


print("[+] starting cracker")



start = perf_counter()

def crack(hashed_password, password):


	extracted_salt = str(salt_extract(hashed_password))
	hashed = create_hash(password, extracted_salt)
	if args.verbose:

		print(f'trying: {password}                                  \r', end='')




	if hashed == hashed_password:
		finish = perf_counter()

		print(f"\n\n[*] password cracked: {password}")
		print(f"[+] finished in {round(finish-start, 2)} second(s)")
		from os import _exit
		_exit(1)






password_list = open(password_lst, 'r', encoding='latin1').readlines()
passwords = [p.strip() for p in password_list]
extracted_salt = str(salt_extract(hashed_password))
print(f"[+] extracted salt: {extracted_salt}")
print(f"[+] using {len(password_list)} password")
hash_id(extracted_salt)


try:

	with ProcessPoolExecutor(args.processors) as ex:
		result = [ex.submit(crack, hashed_password, password) for password in passwords]

except:
	pass