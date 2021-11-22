'''
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать
результаты из байтовового в строковый тип на кириллице.
'''


import platform
import subprocess
from chardet import detect


def ping(host: str) -> bytes:
    params = '-n' if platform.system().lower() == 'windows' else '-c'
    args = ['ping', params, '4', host]
    return subprocess.Popen(args, stdout=subprocess.PIPE)


def decode_ping_response(response: bytes):
    for line in response.stdout:
        line = line.decode(detect(line)['encoding']).encode('utf-8')
        print(line.decode('utf-8'))


if __name__ == '__main__':
    URLS = ['yandex.ru', 'www.youtube.com']
    for url in URLS:
        decode_ping_response(ping(url))
        print('=' * 80)

