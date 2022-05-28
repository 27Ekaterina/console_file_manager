from functions import *

'''
написать тесты для встроенных функций filter, map, sorted,
а также для функций из библиотеки math: pi, sqrt, pow, hypot
'''

'''
тестирование filter
'''
def test_filter_numbers():
    for nums in filter_numbers:
        assert nums > 10

def test_filter_number():
    x = []
    for i in filter_number:
        x.append(i)
    assert len(x) == 4

def test_fil_number_operate():
    assert num[0] not in fil_number_operate

'''
тестирование map
'''
def test_kilometer_distances():
    mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
    assert kilometer_distances[0] / 1.6 == mile_distances[0]
    assert kilometer_distances[1] / 1.7 != mile_distances[1]

def test_kilometer():
    assert kilometer[0]/mile_distances[0] == 1.6

'''
тестирование sorted
'''
def test_new_list():
    assert new_list[2] > new_list[1] > new_list[0]

def test_sort_friends():
    assert sort_friends[0] == "Аня"

'''
тестирование math.pi
'''
import math

def test_square():
    assert float('{:.3f}'.format(square(2))) == 12.566
    assert square(2)/math.pi == 4

'''
тестирование math.sqrt
'''
def test_my_number():
    assert my_number(25) ** 2 == 25

'''
тестирование math.sqrt
'''
def test_my_number_in_degree():
    assert my_number_in_degree(2, 3) == 8

'''
тестирование math.hypot
'''
def test_my_number_hyp():
    assert float('{:.3f}'.format(my_number_hyp(4, 1))) == 4.123

