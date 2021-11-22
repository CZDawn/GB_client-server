'''
Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt,
info_2.txt, info_3.txt и формирующий новый «отчетный» файл
в формате CSV. Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор
файлов с данными, их открытие и считывание данных. В этой функции из
считанных данных необходимо с помощью регулярных выражений извлечь
значения параметров «Изготовитель системы», «Название ОС»,
«Код продукта», «Тип системы». Значения каждого параметра поместить
в соответствующий список. Должно получиться четыре списка — например,
os_prod_list, os_name_list, os_code_list, os_type_list. В этой же
функции создать главный список для хранения данных отчета — например,
main_data — и поместить в него названия столбцов отчета в виде списка:
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в
файл main_data (также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции
get_data(), а также сохранение подготовленных данных в соответствующий
CSV-файл;

Проверить работу программы через вызов функции write_to_csv().
'''


import re
import csv
from chardet import detect


def get_data(files_list: list) -> list:
    main_data = [
        [
            'Изготовитель системы',
            'Название системы',
            'Код продукта',
            'Тип системы'
        ],
    ]
    os_product_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    i = 0
    for file_ in files_list:
        with open(file_, 'rb') as file:
            content = file.read()
        with open(file_, 'w', encoding='utf-8') as file:
            file.write(content.decode(detect(content)['encoding']))
        with open(file_, encoding='utf-8') as file:
            for line in file:
                if re.match(r'Изготовитель системы', line):
                    os_product_list.append(line.split(':')[1].strip())
                if re.match(r'Название ОС', line):
                    os_name_list.append(line.split(':')[1].strip())
                if re.match(r'Код продукта', line):
                    os_code_list.append(line.split(':')[1].strip())
                if re.match(r'Тип системы', line):
                    os_type_list.append(line.split(':')[1].strip())
        main_data.append([os_product_list[i], \
                          os_name_list[i], \
                          os_code_list[i], \
                          os_type_list[i]])
        i += 1
    return main_data


def write_to_csv(data: list):
    with open('main_data.csv', 'w') as file:
        csv.writer(file).writerows(data)


if __name__ == '__main__':
    FILES_LIST = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    write_to_csv(get_data(FILES_LIST))

