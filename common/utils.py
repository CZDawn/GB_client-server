import json
from socket import socket

from .veriables import DEFAULT_MAX_PACKAGE_LENGTH, DEFAULT_ENCODING
from decorators import log_deco


@log_deco
def get_message(sender: str):
    obtained_message = sender.recv(DEFAULT_MAX_PACKAGE_LENGTH)
    if isinstance(obtained_message, bytes):
        json_response = obtained_message.decode(DEFAULT_ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


@log_deco
def send_message(addressee: str, message: str):
    json_message = json.dumps(message)
    encoded_message = json_message.encode(DEFAULT_ENCODING)
    addressee.send(encoded_message)

