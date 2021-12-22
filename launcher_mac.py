import os
import time
from subprocess import Popen

CHOICES = """
1 - запуск сервера
2 - остановка сервера
3 - запуск 4 клиентов
4 - остановка клиентов
5 - остановить все и выйти
Выберите действие: """

CLIENTS = []
SERVER = ''
PATH_TO_FILE = os.path.dirname(__file__)
PATH_TO_SCRIPT_SERVER = os.path.join(PATH_TO_FILE, "server.py")
PATH_TO_SCRIPT_CLIENTS = os.path.join(PATH_TO_FILE, "client.py")

while True:
    CHOICE = input(CHOICES)

    if CHOICE == '1':
        print("Run the server")
        SERVER = Popen(
            f'osascript -e \'tell application "Terminal" to do '
            f'script "python3 {PATH_TO_SCRIPT_SERVER}"\'',
            shell=True
        )
    elif CHOICE == '2':
        # pass
        print("Убили сервер")
        SERVER.kill()
    elif CHOICE == '3':
        print("Run clients")
        for i in range(2):
            CLIENTS.append(
                Popen(
                    f'osascript -e \'tell application "Terminal" to do '
                    f'script "python3 {PATH_TO_SCRIPT_CLIENTS}"\'',
                    shell=True))
            time.sleep(0.5)
    elif CHOICE == '4':
        for i in range(len(CLIENTS)):
            print(CLIENTS[i])
            CLIENTS[i].kill()
    elif CHOICE == '5':
        # break
        for i in range(len(CLIENTS)):
            CLIENTS[i].kill()
        SERVER.kill()
        break

