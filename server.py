import sys
import json
import socket
import logging

# Import project settings
from common.veriables import DEFAULT_ADDRESS, DEFAULT_PORT, \
                             DEFAULT_ENCODING, DEFAULT_MAX_PACKAGE_LENGTH, \
                             DEFAULT_MAX_CONNECTIONS, ACTION, TIME, USER, \
                             ACCOUNT_NAME, PRESENCE, RESPONSE, ERROR, \
                             RESPONDEFAULT_IP_ADDRESSEE
# Import project utils
from common.utils import get_message, send_message

# Import logger config
from log import server_log_config


LOG = logging.getLogger('server_logger')


class Server(socket.socket):
    def __init__(self, listening_address, listening_port):
        super(Server, self).__init__(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        self.listening_address = listening_address
        self.listening_port = listening_port
        LOG.debug('START SERVER: Server is listening!')

    def messages_handler(self):
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.bind((self.listening_address, self.listening_port))
        self.listen(DEFAULT_MAX_CONNECTIONS)
        while True:
            self.client, self.addr = self.accept()
            message = get_message(self.client)
            LOG.debug(f'CLIENT MESSAGE: Получено сообщение от клиента {message}')
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
            LOG.debug(f'SERVER RESPONSE: {response} was sended!')
            self.client.close()


def main():
    # Проверяем указанный IP адрес
    try:
        if '-a' in sys.argv:
            listening_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listening_address = '0.0.0.0'
    except IndexError:
        LOG.error('ERROR: Не указан слушаемый IP адрес после параметра "-а"!')
        sys.exit(1)

    # Проверряем указанный порт
    try:
        if '-p' in sys.argv:
            listening_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listening_port = DEFAULT_PORT
        if listening_port < 1024 or listening_port > 65535:
            raise ValueError
    except IndexError:
        LOG.error('ERROR: Не указан номер порта после параметра "-р"!')
        sys.exit(1)
    except ValueError:
        LOG.error('ERROR: Указан порт вне диапазона от 1024 до 65535!')
        sys.exit(1)

    SERVER_OBJECT = Server(listening_address, listening_port)
    SERVER_OBJECT.messages_handler()


if __name__ == '__main__':
    main()

