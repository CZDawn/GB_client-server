'''
Задание на закрепление знаний по модулю yaml. Написать скрипт,
автоматизирующий сохранение данных в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь,где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке ASCII
(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы с
юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
'''


import yaml


def write_data_to_yaml(values_to_write: dict):
    with open('file.yaml', 'w', encoding='utf-8') as file:
        yaml.dump(values, file, default_flow_style=False, allow_unicode=True)


if __name__ == '__main__':
    FIRST_KEY = [1, 2, 3]
    SECOND_KEY = 100
    THIRD_KEY = {'€': {'unicode_code': 8364}}
    values = {'first_key': FIRST_KEY, 'second_key': SECOND_KEY, 'third_key': THIRD_KEY}
    write_data_to_yaml(values)
