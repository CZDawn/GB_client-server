import os
import sys
import json
import unittest
sys.path.append(os.path.join(os.getcwd(), '..'))

from common.veriables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, \
                             ACTION, PRESENCE, DEFAULT_ENCODING, \
                             DEFAULT_MAX_PACKAGE_LENGTH
from common.utils import get_message, send_message


class TestSocket:
    def __init__(self, test_message: dict):
        self.test_message = test_message
        self.encoded_message = None
        self.obtained_message = None

    def send(self, sending_message):
        json_message = json.dumps(self.test_message)
        self.encoded_message = json_message.encode(DEFAULT_ENCODING)
        self.obtained_message = sending_message

    def recv(self, DEFAULT_MAX_PACKAGE_LENGTH):
        json_message = json.dumps(self.test_message)
        return json_message.encode(DEFAULT_ENCODING)


class TestUtils(unittest.TestCase):
    test_message_to_send = {
        ACTION: PRESENCE,
        TIME: 123,
        USER: {
            ACCOUNT_NAME: 'Test Guest'
        }
    }
    test_message_obtained_ok = {RESPONSE: 200}
    test_message_obtained_err = {
        RESPONSE: 400,
        ERROR: 'Bad request'
    }

    def test_sending_message(self):
        test_socket = TestSocket(self.test_message_to_send)
        send_message(test_socket, self.test_message_to_send)
        self.assertEqual(
            test_socket.encoded_message,
            test_socket.obtained_message
        )

    def test_getting_message(self):
        test_socket_ans_ok = TestSocket(self.test_message_obtained_ok)
        test_socket_ans_err = TestSocket(self.test_message_obtained_err)
        self.assertEqual(
            get_message(test_socket_ans_ok),
            self.test_message_obtained_ok
        )
        self.assertEqual(
            get_message(test_socket_ans_err),
            self.test_message_obtained_err
        )

if __name__ == '__main__':
    unittest.main()

