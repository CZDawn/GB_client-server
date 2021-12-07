import os
import sys
import time
import socket
import unittest
import threading

sys.path.append(os.path.join(os.getcwd(), '..'))

from server import Server
from common.veriables import DEFAULT_ADDRESS, DEFAULT_PORT


class TestServer(unittest.TestCase):
    def test_game_server_starts_tcp_server(self):
        # Start server in a background thread
        server = Server(DEFAULT_ADDRESS, DEFAULT_PORT)
        server_thread = threading.Thread(target=server.messages_handler)
        server_thread.start()

        # 0.0000001 is the minimum sleep time or the client might connect 
        # before server thread binds and listens.        
        time.sleep(0.000001)

        # This is our fake test client that is just going to attempt a connect and disconnect
        fake_client = socket.socket()
        fake_client.settimeout(1)
        fake_client.connect((DEFAULT_ADDRESS, DEFAULT_PORT))
        fake_client.close()

        # Make sure server thread finishes
        server_thread.join(3)


if __name__ == '__main__':
    unittest.main()

