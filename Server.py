import sys
import json
import socket

# Import project settings
from settings import DEFAULT_ADDRESS, DEFAULT_PORT, DEFAULT_ENCODING, \
                     DEFAULT_MAX_PACKAGE_LENGTH, DEFAULT_MAX_CONNECTIONS, \
                     ACTION, TIME, USER, ACCOUNT_NAME, PRESENCE, RESPONSE, \
                     ERROR, RESPONDEFAULT_IP_ADDRESSEE
# Import project utils
from utils import get_message, send_message


class Server(socket.socket):
    def __init__(self, listen_address, listen_port):
        super(Server, self).__init__(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.bind((listen_address, listen_port))
        self.listen(DEFAULT_MAX_CONNECTIONS)
        print('Server is listening!')

    def __client_message_handler(self, message):
        if ACTION in message and message[ACTION] == PRESENCE \
                  and TIME in message and USER in message \
                  and message[USER][ACCOUNT_NAME] == 'Guest':
                      return {RESPONSE: 200}
        return {
            RESPONSEFAULT_IP_ADDRESSEE: 400,
            ERROR: 'Bad request'
        }

    def answer_for_messages(self, sender=None):
        while True:
            sender, sender_addr = self.accept()
        try:
            client_message = get_message(sender)
            response = self.__client_message_handler(client_message)
            send_message(sender, response)
            sender.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорректное сообщение от клиента.')
            sender.close()


def main():
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 and listen_port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра "-p" необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print('Значение порта должно быть в диапазоне от 1024 до 65535.')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = '0.0.0.0'
    except IndexError:
        print('После параметра "-a" необходимо указать адрес, который будет слушать сервер.')
        sys.exit(1)

    server_obj = Server(listen_address, listen_port)
    server_obj.answer_for_messages()


if __name__ == '__main__':
    main()
