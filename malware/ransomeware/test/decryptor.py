# Advanced Ransomeware decryptor
import os
import socket
import hashlib
from threading import Thread
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

encrypted_ext = ('.txt',)

file_paths = []
for root, dir, files in os.walk('/root/Desktop/test'):
	for file in files:
		file_path, file_ext = os.path.splitext(root+'/'+file)
		if file_ext in encrypted_ext:
			file_paths.append(root+'/'+file)



def reborn():
	keyRSA = RSA.importKey(open('private.pem').read())
	cipher = PKCS1_OAEP.new(keyRSA)
	for file in file_paths:
		print(f'[*] Decrypting {file} with RSA')
		with open(file, 'rb') as df:
			data = df.read()
		with open(file, 'wb') as d:
			decrypted = cipher.decrypt(data)
			d.write(decrypted)

	password = b"fsocietyencryptingtheworld"
	keyAES = hashlib.sha256(password).digest()
	IV = 'ThisisanIV456aaa'.encode()
	cipher = AES.new(keyAES,AES.MODE_CBC,IV)
	for file in file_paths:
		print(f'[*] Decrypting {file} with AES')
		with open(file, 'rb') as f:
			data = f.read()
		with open(file, 'wb') as en:
			decrypted_data = cipher.decrypt(data)
			en.write(decrypted_data)

reborn()