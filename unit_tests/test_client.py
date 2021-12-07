import os
import sys
import socket
import unittest
import threading

sys.path.append(os.path.join(os.getcwd(), '..'))

from client import Client
from common.veriables import DEFAULT_ADDRESS, DEFAULT_PORT


class TestClient(unittest.TestCase):
    def run_fake_server(self):
        # Run a server to listen for a connection and then close it
        server_sock = socket.socket()
        server_sock.bind((DEFAULT_ADDRESS, DEFAULT_PORT))
        server_sock.listen(0)
        server_sock.accept()
        server_sock.close()

    def test_client_connects_and_disconnects_to_fake_server(self):
        # Start fake server in background thread
        server_thread = threading.Thread(target=self.run_fake_server)
        server_thread.start()

        # Test the clients basic connection and disconnection
        fake_client = Client(DEFAULT_ADDRESS, DEFAULT_PORT)
        fake_client.close()

        # Ensure server thread ends
        server_thread.join(3)


if __name__ == '__main__':
    unittest.main()

