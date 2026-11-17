import ftplib

HOST = "tsi4-tellus"
PORT = 21

animal = input("Digite o animal (usuário): ")
senha = animal + "2026"

# Conecta e autentica
ftp = ftplib.FTP()
ftp.connect(HOST, PORT)
print(ftp.getwelcome())

print(ftp.login(user=animal, passwd=senha))

# PWD - exibe o diretório atual
print("\n--- PWD ---")
print(ftp.pwd())

# CDUP - sobe um nível de diretório (primeira vez)
print("\n--- CDUP ---")
print(ftp.cwd(".."))

# CDUP - sobe mais um nível (segunda vez)
print("\n--- CDUP ---")
print(ftp.cwd(".."))

# MKD - cria o diretório /srv/pub/{animal}
print(f"\n--- MKD /srv/pub/{animal} ---")
print(ftp.mkd(f"/srv/pub/{animal}"))

# CWD - entra no diretório criado
print(f"\n--- CWD /srv/pub/{animal} ---")
print(ftp.cwd(f"/srv/pub/{animal}"))

# DELE - deleta lorem.jpg
print("\n--- DELE lorem.jpg ---")
print(ftp.delete("lorem.jpg"))

# DELE - deleta ipsum.mp4
print("\n--- DELE ipsum.mp4 ---")
print(ftp.delete("ipsum.mp4"))

# QUIT - encerra a sessão
print("\n--- QUIT ---")
print(ftp.quit())
