import os
import datetime
import shutil

now = datetime.datetime.now()
hoje = now.strftime("%Y-%m-%d")
base = "C://Projetos//Arquivos de midia//Para descarte//"
pastas = os.listdir(base)

for pasta in pastas:
    print(pasta)
    print(datetime.datetime.strptime(pasta, '%Y-%m-%d') <= now)

