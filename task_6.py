'''
Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор». Проверить кодировку
файла по умолчанию. Принудительно открыть файл в формате Unicode и
вывести его содержимое.
'''


from chardet import detect


def write_file_of_strings(strings: list):
    ''' Записывает файл в кодировке, отличной от UTF-8 (cp1251) '''

    with open('test_file.txt', 'w', encoding='cp1251') as file:
        for string_ in strings:
            file.write(f'{string_}\n')


def open_file_in_any_encoding(path_: str):
    with open(path_, 'rb') as file:
        content = file.read()
    with open(path_, 'w', encoding='utf-8') as file:
        file.write(content.decode(detect(content)['encoding']))
    with open(path_, encoding='utf-8') as file:
        print(f'Содержимое файла: \n{file.read()}')
        print('=' * 50)


if __name__ == '__main__':
    LIST_OF_STRINGS = ['сетевое программирование', 'сокет', 'декоратор']
    write_file_of_strings(LIST_OF_STRINGS)
    open_file_in_any_encoding('test_file.txt')

