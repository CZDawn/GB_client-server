'''
Каждое из слов «разработка», «сокет», «декоратор» представить
в строковом формате и проверить тип и содержание соответствующих
переменных. Затем с помощью онлайн-конвертера преобразовать строковые
представления в формат Unicode и также проверить тип и содержимое
переменных.
'''


def check_type_and_content_of_list_elements(values: list):
    ''' Выводит в консоль тип и содержание каждого элемента списка '''

    print('Тип и содержание элементов списка: \n')
    for value in values:
        print(f'Content: {value}, Type: {type(value)}')
    print('=' * 50)


if __name__ == '__main__':
    WORDS_IN_STRING_FORMAT = [
        'разработка',
        'сокет',
        'декоратор'
    ]
    WORDS_IN_UNICODE_FORMAT = [
        '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
        '\u0063\u043e\u043a\u0435\u0442',
        '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
    ]

    check_type_and_content_of_list_elements(WORDS_IN_STRING_FORMAT)
    check_type_and_content_of_list_elements(WORDS_IN_UNICODE_FORMAT)

