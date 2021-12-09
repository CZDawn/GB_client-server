import sys
import json
import socket

# Import project settings
from common.veriables import DEFAULT_ADDRESS, DEFAULT_PORT, \
                             DEFAULT_ENCODING, DEFAULT_MAX_PACKAGE_LENGTH, \
                             DEFAULT_MAX_CONNECTIONS, ACTION, TIME, USER, \
                             ACCOUNT_NAME, PRESENCE, RESPONSE, ERROR, \
                             RESPONDEFAULT_IP_ADDRESSEE
# Import project utils
from common.utils import get_message, send_message


class Server(socket.socket):
    def __init__(self, listening_address=None, listening_port=None):
        super(Server, self).__init__(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        self.listening_address = listening_address
        self.listening_port = listening_port
        print('Server is listening!')

    def messages_handler(self):
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.bind((self.listening_address, self.listening_port))
        self.listen(DEFAULT_MAX_CONNECTIONS)
        while True:
            self.client, self.addr = self.accept()
            message = get_message(self.client)
            if ACTION in message and message[ACTION] == PRESENCE \
                      and TIME in message and USER in message \
                      and message[USER][ACCOUNT_NAME] == 'Guest':
                response = {RESPONSE: 200}
            else:
                response = {
                    RESPONDEFAULT_IP_ADDRESSEE: 400,
                    ERROR: 'Bad request'
                }
            send_message(self.client, response)
            print(f'{response} was sended!')
            self.client.close()


def main():
    # Проверяем указанный IP адрес
    try:
        if '-a' in sys.argv:
            _host = sys.argv[sys.argv.index('-a') + 1]
        else:
            _host = '0.0.0.0'
    except IndexError:
        print('После параметра "-a" необходимо указать слушаемый IP адрес!')
        sys.exit(1)

    # Проверряем указанный порт
    try:
        if '-p' in sys.argv:
            _port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            _port = DEFAULT_PORT
        if _port < 1024 or _port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра "-p" необходимо указать номер порта!')
        sys.exit(1)
    except ValueError:
        print('Порт должен быть в диапазоне от 1024 до 65535!')
        sys.exit(1)

    SERVER_OBJECT = Server(listening_address=_host, listening_port=_port)
    SERVER_OBJECT.messages_handler()


if __name__ == '__main__':
    main()

