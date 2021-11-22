'''
Каждое из слов «class», «function», «method» записать в байтовом
типе без преобразования в последовательность кодов (не используя
методы encode и decode) и определить тип, содержимое и длину
соответствующих переменных.
'''

import struct


def convert_word_to_bytes(word: str) -> bytes:
    word_in_list_format = []
    for letter in word:
        unicode_code = ord(letter)
        if unicode_code < 255:
            word_in_list_format.append(struct.pack('B', unicode_code))
        elif unicode_code < 65535:
            word_in_list_format.append(struct.pack('>H', unicode_code))
        else:
            b = (unicode_code & 0xFF0000) >> 16
            H = unicode_code & 0xFFFF
            word_in_list_format.append(struct.pack('>bH', b, H))
    return b''.join(word_in_list_format)


def convert_list_of_words_to_bytes(words: list) -> list:
    return [convert_word_to_bytes(word) for word in words]


def find_type_content_and_length_in_bytes(values: list):
    for value in values:
        print(f'Content of value: {value}:')
        print(f'1. Type of content: {type(value)};')
        print(f'2. Length of content in bytes: {len(value)}.')
        print('=' * 50)


if __name__ == '__main__':
    WORDS = ['class', 'function', 'method']

    find_type_content_and_length_in_bytes(convert_list_of_words_to_bytes(WORDS))

