'''
Задание на закрепление знаний по модулю json.
Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:

Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать
запись данных в виде словаря в файл orders.json. При записи данных
указать величину отступа в 4 пробельных символа;

Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.
'''


import json


def write_order_to_json(item: str, quantity: int, price: float, buyer: str, date: str):
    data = {
        'product': item,
        'quantity': quantity,
        'price': price,
        'customer': buyer,
        'date': date
    }
    with open('orders.json', encoding='utf-8') as file:
        content = json.load(file)
        content['orders'].append(data)
    with open('orders.json', 'w', encoding='utf-8') as file:
        json.dump(content, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    write_order_to_json('printer', 5, 5340.50, 'Василий', '20.11.2021')

