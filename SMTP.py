import smtplib

HOST = "localhost"
PORT = 25

animal = input("Digite o animal (remetente): ")
colega = input("Digite o colega (destinatário): ")
mensagem = input("Digite a mensagem: ")

remetente = f"{animal}@anima.lab"
destinatario = f"{colega}@anima.lab"

# Monta o corpo do e-mail com cabeçalhos
corpo = f"From: {remetente}\r\nTo: {destinatario}\r\nSubject: Uma mensagem animal\r\n\r\n{mensagem}"

# Conecta ao servidor SMTP
servidor = smtplib.SMTP(HOST, PORT)

# EHLO
servidor.ehlo("tellus.anima.lab")

# MAIL FROM, RCPT TO, DATA
servidor.sendmail(remetente, destinatario, corpo)
print("E-mail enviado com sucesso!")

# QUIT
servidor.quit()
