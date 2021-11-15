#!/usr/bin/python3
# gmail sender name spoofer

import smtplib
import sys


try:
	myemail = "fsociety.py00@gmail.com"
	mypassword = '15104cce5a876c75af70b2e03b44d37fdeb30af1b6cabf24050fa415e56969ba'

	fakefrom = 'friend@fsociety.com'
	fakename = sys.argv[2]

	to_email = sys.argv[4]
	print("[*] starting spoofer...")
	print("\t")

	to_name = 'lucifer '

	subject = input("[+] Enter the email's Subject: ")

	content = input("[+] Enter the email's content: ")

	message = f'From: {fakename} <root@fsociety.com>\nTo:  <{to_email}>\nSubject: {subject}\n\n{content}'

	server = smtplib.SMTP('smtp.gmail.com', 587)

	print("[*] started smtp gmail server")
	server.ehlo()
	server.starttls()

	print("[*] started secure tunnel with tls")

	login = server.login(myemail, mypassword)

	if login:
		print("[*] logged in successfully")


	print(f"[*] sending email with name {fakename} ")
	server.sendmail(myemail, to_email, message)



	print(f"[*] email should be sent to {to_email}")

	server.close()

except IndexError:
	print("[-] usage: ./spoofer.py --name <name_to_send_as> --email-to <gmail_to_send_to> ")