import sys
import json
import socket

from time import time

# Import project settings
from settings import DEFAULT_ADDRESS, DEFAULT_PORT, DEFAULT_ENCODING, \
                     DEFAULT_MAX_PACKAGE_LENGTH, DEFAULT_MAX_CONNECTIONS, \
                     ACTION, TIME, USER, ACCOUNT_NAME, PRESENCE, RESPONSE, \
                     ERROR, RESPONDEFAULT_IP_ADDRESSEE
# Import project utils
from utils import get_message, send_message


class Client(socket.socket):
    def __init__(self, server_address, server_port):
        super(Client, self).__init__(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        self.server_address = server_address
        self.server_port = server_port
        self.connect((self.server_address, self.server_port))
        print('Client is set up!')

    def __create_presence_message(self, account_name='Guest'):
        out_message = {
            ACTION: PRESENCE,
            TIME: time(),
            USER: {
                ACCOUNT_NAME: account_name
            }
        }

        return out_message

    def server_answer_handler(self, message):
        if RESPONSE in message:
            if message[RESPONSE] == 200:
                return '200: OK'
            return f'400: {message[ERROR]}'

    def send_presence_message_to_server(self):
        message = self.__create_presence_message()
        send_message(self, message)


def main():
    try:
        server_address = sys.argv[1]
        server_port = sys.argv[2]
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        print('Значение номера порта должно быть в диапазоне от 1024 до 65535.')
        sys.exit(1)

    client_obj = Client(server_address, server_port)
    client_obj.send_presence_message_to_server()

    try:
        server_answer = client_obj.server_answer_handler(get_message(client_obj))
        print(server_answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()

