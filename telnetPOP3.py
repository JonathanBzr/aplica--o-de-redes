import poplib

HOST = "tsi4-tellus"
PORT = 100

usuario = input("Digite o usuário: ")
senha = usuario + "2026"

# Conecta ao servidor POP3
servidor = poplib.POP3(HOST, PORT)
print(servidor.getwelcome().decode("ascii"))

# USER e PASS
print(servidor.user(usuario).decode("ascii"))
print(servidor.pass_(senha).decode("ascii"))

# LIST - lista todas as mensagens
print("\n--- LIST ---")
resposta, lista, tamanho = servidor.list()
print(resposta.decode("ascii"))
for item in lista:
    print(item.decode("ascii"))

# RETR - recupera uma mensagem
num = int(input("\nNúmero da mensagem para RETR: "))
print(f"\n--- RETR {num} ---")
resposta, linhas, bytes_totais = servidor.retr(num)
print(resposta.decode("ascii"))
for linha in linhas:
    print(linha.decode("ascii"))

# DELE - deleta uma mensagem
num = int(input("\nNúmero da mensagem para DELE: "))
print(f"\n--- DELE {num} ---")
print(servidor.dele(num).decode("ascii"))

# RSET - desfaz as deleções marcadas
print("\n--- RSET ---")
print(servidor.rset().decode("ascii"))

# QUIT - encerra a sessão
print("\n--- QUIT ---")
print(servidor.quit().decode("ascii"))
