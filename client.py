import sys
import json
import time
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
from logs import client_log_config


LOG = logging.getLogger('client_logger')


class Client(socket.socket):
    def __init__(self, server_address, server_port):
        super(Client, self).__init__(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        self.server_address = server_address
        self.server_port = server_port

    def server_response_handler(self):
        response = get_message(self)
        if RESPONSE in response:
            LOG.debug('SERVER RESPONSE: answer code - 200: Ok')
        else:
            LOG.error(f'ERROR: answer code - 400: {json_answer[ERROR]}')

    def sending_presence_message(self):
        self.connect((self.server_address, self.server_port))
        message = {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: 'Guest'
            }
        }
        send_message(self, message)
        LOG.debug('CLIENT MESSAGE: Client send the presence message to server!')
        self.server_response_handler()
        self.close()


def main():
    # Проверряем указанные IP адрес и порт сервера
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        LOG.error('ERROR: Указан порт вне диапазона от 1024 до 65535!')
        sys.exit(1)

    CLIENT_OBJECT = Client(server_address, server_port)
    CLIENT_OBJECT.sending_presence_message()


if __name__ == '__main__':
    main()

