# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 14:04:26 2015

@author: papacheco
"""

#!/usr/bin/python
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
#from email.mime.text import MIMEText
from email import Encoders
import os
import csv
texto_msg = '''
Presado usuario(a) %(nome)s !!!
Este e um email enviado por um script PYTHON =D, seu email deve ficar aqui!!
'''
user = "pedro.pacheco.a@gmail.com"
pwd = "***********"
anexo = "/home/papacheco/anexo.txt" #Caminho do anexo a ser enviado
def process(row, to, subject, text, attach):
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = row[0]
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
part = MIMEBase('application', 'octet-stream')
part.set_payload(open(anexo,'rb').read())
Encoders.encode_base64(part)
part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(anexo))
msg.attach(part)
mailServer = smtplib.SMTP("smtp.gmail.com", 587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login(user, pwd)
mailServer.sendmail(user, to, msg.as_string())
mailServer.close()
if __name__ == '__main__':
    lista = open('/home/papacheco/lista.csv') #Caminho da lista de email CSV
    csv_reader = csv.reader(lista)
for row in csv_reader:
    process(row, user,"Enviando Email com Python", texto_msg % {'nome':row[1]}, anexo)
    lista.close()
