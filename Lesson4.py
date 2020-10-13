# Задача №1
from sys import argv

script_name, first_param, second_param, third_param = argv
print("Выработка в часах: ", first_param)
print("Ставка в час: ", second_param)
print("Премия: ", third_param)


def payroll(first_param, second_param, third_param):
    try:
        first_param, second_param, third_param = float(first_param), float(second_param), float(third_param)
        pay_sum = first_param * second_param + third_param
    except ValueError:
        return "Напишите три цифры в числовом формате"
    return pay_sum


print("Заработная плата равна:", payroll(first_param, second_param, third_param))

# Задача №2 (так работает, сделать в генераторе)
list2 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list2 = []
for i in range(1, len(list2)):
    if list2[i] > list2[i - 1]:
        new_list2.append(list2[i])
print(new_list2)

# в генераторе:
list2 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list2 = [list2[i] for i in range(1, len(list2)) if list2[i] > list2[i - 1]]
print(new_list2)


# Задача №3
list3 = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(list3)


# Задача №4
list4 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list4 = [el for el in list4 if list4.count(el) == 1]
print(new_list4)


# Задача №5
from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, [i for i in range(100, 1001) if i % 2 == 0]))


# Задача №6
from itertools import count
from itertools import cycle

digit = int(input("Укажите число с которого начать:"))
end = int(input("Укажите число которым закончить:"))
qua = int(input("Количество повторений:"))
a = []
for el in count(digit):
    if el > end:
        break
    else:
        a.append(el)

m = 0
for j in cycle(a):
    if m > qua:
        break
    print(j)
    m += 1


# Задача №7
from math import factorial
what = int(input("Укажите число которым закончить:"))
generator = (factorial(param) for param in range(1, what+1))
for el in generator:
    print(el)
