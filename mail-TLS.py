#encoding: utf-8
#importamos os módulos necessários
import smtplib
from email.mime.text import MIMEText
#cria um cliente smtp que conectará em smtp.gmail.com na porta 587
gm = smtplib.SMTP("mail.furb.br", 587)
#nos identificamos no servidor
gm.ehlo()
#indicamos que usaremos uma conexão segura
gm.starttls()
#reidentificamos no servidor (necessário apos starttls )
gm.ehlo()
#faz o login
gm.login("papacheco@furb.br", "*************") 
#Cria um email contendo texto e guarda em mail
mail = MIMEText("Python enviou este email")
#Seta destinatário e assunto
mail["To"] = "suporte@furb.br"
mail["Subject"] = "Assunto aqui"
#Envia o email. 
gm.sendmail("papacheco@furb.br", "papacheco@furb.br", mail.as_string())
#fecha a conexão
gm.close()

