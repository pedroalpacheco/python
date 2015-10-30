#!/usr/bin/env python

import smtplib

host = 'mail.furb.br'
port = '587'
user = 'papacheco@furb.br'
passw = '**********senha'

server = smtplib.SMTP()
server.connect(host, port)
server.ehlo()
server.starttls()
server.login(user, passw)

notice = "Completed"
tolist = ["user@somewhere.com"]
fromaddr = '"IT Staff" '
subject = 'Oracle server maintenance notice'
message = '''

The Oracle database server maintenance is

%s

''' % notice

hdr = "From: %s\r\nTo: %s\r\nSubject: %s\r\nX-Mailer: My-Mail\r\n\r\n" % (fromaddr, tolist, subject)
server.sendmail("it@vlsmaps.com", tolist, hdr+message)
server.quit
