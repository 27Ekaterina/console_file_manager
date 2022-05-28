"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

import json
import os
from separator import add_separators

@add_separators
def run_bill():
    """
    Функция запускает программу личный счет
    :return:
    """
    bill_sum = 0
    history = []

    FILE_NAME = "my_count.json"
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            history = json.load(f)

    FILE_NAME_sum = "my_money.json"
    if os.path.exists(FILE_NAME_sum):
        with open(FILE_NAME_sum, 'r') as f:
            bill_sum = json.load(f)
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(f'Ваш счет {bill_sum}')

        choice = input('Выберите пункт меню')
        if choice == '1':
            try:
                cost = int(input('Введите сумму'))
                bill_sum += cost
            except ValueError:
                print("Cумму взноса нужно вводить цифрами!")
        elif choice == '2':
            try:
                cost = int(input('Введите сумму покупки'))
                if cost > bill_sum:
                    print('Недостаточно средств')
                else:
                    bill_sum -= cost
                    name = input('Введит название покупки')
                    history.append((name, cost))
            except ValueError:
                print("Cумму покупки нужно вводить цифрами!")
        elif choice == '3':
            print(history)
        elif choice == '4':
            with open(FILE_NAME, 'w') as f:
                json.dump(history, f)
            with open(FILE_NAME_sum, 'w') as f:
                json.dump(bill_sum, f)
            break
        else:
            print('Неверный пункт меню')

if __name__ == '__main__':
    run_bill()