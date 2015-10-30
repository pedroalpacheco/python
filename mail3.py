import smtplib

smtp = smtplib.SMTP('mail.furb.br', 587)
smtp.starttls()

smtp.login('papacheco@furb.br', '*******')

de = 'papacheco@furb.br'

para = ['papacheco@furb.br']

msg = """From: %sTo: %sSubject: Buteco Open SourceEmail de teste do Buteco Open Source.""" % (de, ', '.join(para))
smtp.sendmail(de, para, msg)
smtp.quit()
