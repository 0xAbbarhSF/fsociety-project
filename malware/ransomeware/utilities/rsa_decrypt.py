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




key = RSA.importKey(open('private.pem').read())
cipher = PKCS1_OAEP.new(key)




for file in file_paths:
	print(f'[+] Decrypting {file} ')
	with open(file, 'rb') as df:
		data = df.read()
	with open(file, 'wb') as d:
		decrypted = cipher.decrypt(data)
		d.write(decrypted)

rm = os.system('rm private.pem')

print(f"[+] deleting private.pem ")





