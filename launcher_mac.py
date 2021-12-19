from os import *
from subprocess import Popen
import subprocess
import time

clients=[]
server=''
pathOfFile=path.dirname(__file__)
pathServer=path.join(pathOfFile, "server.py")
pathReadClient=path.join(pathOfFile, "client.py")
pathSendClient=path.join(pathOfFile, "client_send.py")

while True:
    choice = input(
        "s - запуск сервера, w - остановка сервера, c - запуск 4 клиентов, \
        r - остановка клиентов, t - остановить все, y - остановить все и выйти \n>>>"
    )

    if choice=="s":
        print ("Запустили сервер")
        server = Popen(
            f'osascript -e \'tell application "Terminal" to do'
            f' script "python3 {pathServer}"\'',
            shell=True
        )

    elif choice == "w":
        print ("Убили сервер")
        server.kill()
    elif choice =="c":
            print("Запустили клиенты")
            for i in range(1,3):
                clients.append(Popen(
                    f'osascript -e \'tell application "Terminal" to do'
                    f' script "python3 {pathReadClient}"\'',
                    shell=True
                ))
                time.sleep(0.5)
                clients.append(Popen(
                    f'osascript -e \'tell application "Terminal" to do'
                    f' script "python3 {pathSendClient}"\'',
                    shell=True
                ))

    elif choice == "r":
        for i in range(len(clients)):
            print(clients[i])
            clients[i].kill()
    elif choice == "y":
        for i in range(len(clients)):
            clients[i].kill()
        server.kill()
        break

