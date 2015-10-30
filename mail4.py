import smtplib
 
to = 'papacheco@furb.br'
gmail_user = 'pedro.pacheco.a@gmail.com'
gmail_pwd = '*********************'
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
print header
msg = header + '\n this is test msg from mkyong.com \n\n'
smtpserver.sendmail(gmail_user, to, msg)
print 'done!'
smtpserver.close()
