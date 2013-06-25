#!/usr/bin/python

import smtplib
import logging
import pymysql
import email.utils
from email.mime.text import MIMEText

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', unix_socket='/mysql.sock', passwd='root', db='backend')


cur = conn.cursor()
conn.cursor()
cur.execute("SELECT count(*) FROM table;")

count = cur.fetchone()
count = ''.join(c for c in str(count) if c.isdigit())
count = int(count)

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s',filename='alert.log')


def ToMailOrNot():
    msg = MIMEText('message')
	msg['To'] = email.utils.formataddr(('Recipient', 'me@example.com'))
	msg['From'] = email.utils.formataddr(('Author', 'them@example.com'))
	msg['Subject'] = 'Subject here'
	server = smtplib.SMTP('localhost')
	server.set_debuglevel(True)
	if count <= 100:
		try:
			server.sendmail('me@example.com', ['them@example.com'], msg.as_string())         
			logging.warning('Log message warning level = %s', count)
		finally:
			server.quit()
	else:
		logging.info('Log info level  = %s', count)

ToMailOrNot()
