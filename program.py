'referência: https://stackoverflow.com/questions/32404/how-do-you-run-a-python-script-as-a-service-in-windows'
import os
import datetime
import shutil

def main():
        now = datetime.datetime.now()
        hoje = now.strftime("%Y-%m-%d")
        base = "C://Projetos//Arquivos de midia//Para descarte//"
        pastas = os.listdir(base)

        for pasta in pastas:
                if datetime.datetime.strptime(pasta, '%Y-%m-%d') <= now:
                    shutil.rmtree(base + pasta)

main()
