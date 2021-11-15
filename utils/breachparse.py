#!/usr/bin/python3
# a version similar to heath adams a.k.a (TCM) breachparse.sh in python3

import threading
import os
import sys
import re
import time

try:
	file_paths = []
	query = sys.argv[1]
	database = sys.argv[2]
	breached = []


	def get_files():
		global lock
		lock.acquire()
		try:
			for root, dir, files in os.walk(database):
				for file in files:
					file_paths.append(root+'/'+file)

			if "Compilation" in sys.argv[2] or "compilation" in sys.argv[2]:

				print(f"[*] searching in BreachCompilation database")
				print("[i] this may take a while")
			else:
				print(f"[*] searching in {len(file_paths)} file")
				print("[i] this may take a while")
		finally:
			lock.release()


			
	def get_data():
		global lock
		lock.acquire()
		try:
			for file in file_paths:
				with open(file, 'r', encoding='latin1') as r:
					d = r.read()
					pattern = re.compile(rf'{query}.*')
					match = pattern.findall(d)
					if match:
						info = list(match)
						for x in info:
							breached.append(x)

					else:
						pass
		finally:
			lock.release()
						
	def breach():
		global lock
		lock.acquire()
		try:
			if breached:
				print("\t")
				print("[*] account has been breached")
				print("\t")
				for breach in breached:
					print(breach)
					exit()
			else:
				print("[-] account is not breached!")
		finally:
			lock.release()

	def ThreadPool():

		global lock
		lock = threading.Lock()
		thread1 = threading.Thread(target=get_files)
		thread1.start()
		thread2 = threading.Thread(target=get_data)
		thread2.start()
		thread3 = threading.Thread(target=breach)
		thread3.start()

	ThreadPool()


except IndexError:
	print("[+] usage: python3 breachparse.py EMAIL DATABASE")
	print("[+] example: python3 breachparse.py name@gmail.com /BreachCompilation/data")
	print("[i] DO NOT PUT / AT THE END OF THE DATABASE DIRECTORY")