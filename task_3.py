'''
Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе.
'''


def check_the_word(word: str) -> bool:
    for letter in word:
        unicode_code = ord(letter)
        if unicode_code > 127:
            return False
    return True


def check_list_of_words(words: list) -> dict:
    result_dict = {}
    for word in words:
        result_dict[word] = check_the_word(word)
    return result_dict


if __name__ == '__main__':
    WORDS = ['attribute', 'класс', 'функция', 'type']
    ANSWERS_FOR_TEST_RESULTS = [
        'не может быть записано в байтовом типе',
        'может быть записано в байтовом типе'
    ]

    test_results = check_list_of_words(WORDS)
    for word in WORDS:
        if test_results[word]:
            print(f'Слово "{word}" {ANSWERS_FOR_TEST_RESULTS[1]}.')
        else:
            print(f'Слово "{word}" {ANSWERS_FOR_TEST_RESULTS[0]}.')

