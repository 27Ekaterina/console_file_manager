"""
Функция filter
"""

num = [3, 5.5, 18, 4.1, 79, 15, 7, 18.6]
filter_numbers = filter(lambda x: x > 10, num)

filter_number = filter(lambda x: x < 10, num)

fil_number_operate = [number for number in num if number > 10]

if __name__ == '__main__':
    print(list(filter_numbers))
    print(list(filter_number))
    print(list(fil_number))

"""
Функция map
"""
mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
kilometer_distances = list(map(lambda x: x * 1.6, mile_distances))

kilometer = [mile * 1.6 for mile in mile_distances]

print(kilometer_distances)
print(kilometer)

"""
функция sorted
"""

my_list = [8, 7, 12, 77, 1, 15]
new_list = (sorted(my_list))
print(new_list)

friends = ["Оля", "Вася", "Аня", "Ира"]
sort_friends = sorted(friends)
print(sort_friends)

"""
функции из библиотеки math: pi, sqrt, pow, hypot
"""
import math

"""
функция math.pi (число Пи)
"""
def square(radius):
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    print('Площадь круга равна: ', square(2))
    print(float('{:.3f}'.format(square(2))))

"""
функция math.sqrt (квадратный корень)
"""

def my_number(x):
    return math.sqrt(x)
print(my_number(25))

"""
функция math.pow (возведение в степень)
"""

my_number_in_degree = lambda x, y: math.pow(x, y)

print("Число в степени: ", my_number_in_degree(5, 3))

"""
функция math.hypot (евклидово число)
"""
my_number_hyp = lambda x, y: math.hypot(x, y)

print("Евклидово число: ", my_number_hyp(4, 1))