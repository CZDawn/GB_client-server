'''
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).
'''


def string_to_bytes(string_: str) -> bytes:
    return string_.encode('utf-8')


def bytes_to_string(bytes_: bytes) -> str:
    return bytes_.decode('utf-8')


if __name__ == '__main__':
    WORDS = ['разработка', 'администрирование', 'protocol', 'standard']
    BYTES_LIST = []

    print('Преобразуем слова {WORDS} в байты: ')
    for word in WORDS:
        BYTES_LIST.append(string_to_bytes(word))
        print(f'Строка "{word}" в байтах: {BYTES_LIST[-1]}')

    print('=' * 100)

    print('Преобразуем байты {BYTES_LIST} в строки: ')
    for bytes_ in BYTES_LIST:
        print(f'Байты "{bytes_} в строковом виде: {bytes_to_string(bytes_)}')

