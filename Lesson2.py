# Задача №1
my_list = [1, 2.0, 'dream', 'come', True]
for i in range(len(my_list)):
    print(type(my_list[i]))

# Задача №2
a = []
n = int(input('Введите количество элементов:'))
for i in range(n):
    new_element = input('Элемент')
    a.append(new_element)
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(a)

# Задача №3
month = int(input('Введите номер месяца (от 1 до 12):'))
year = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
print(year.get(month))

# Задача №4
words = input('Введите какие-то очень важные слова:')
list_of_words = words.split()
for ind, el in enumerate(list_of_words, 1):
    print(ind, el[:10])

# Задача №5
rating = [108, 65, 13, 2, 0]
x = int(input('Введите любое натуральное число:'))
rating.append(x)
rat = sorted(rating, reverse = True)
print(rat)

# Задача №6
catalog = []
np = int(input('Сколько позиций?'))
for i in range(np):
    number = int(input('Номер товара:'))
    name = input('Наименование товара:')
    price = int(input('Цена:'))
    quantity = int(input('Количество товара:'))
    item = input('Единица измерения:')
    position = {'название': name, 'цена': price, 'количество': quantity, 'ед.': item}
    position_n = (number, position)
    print(position_n)
    catalog.append(position_n)
print(catalog)

# дальше мой мозг сломался…
# for i in range(catalog):
#     catalog.remove[i](0)
#     print(catalog)

#     catalog.get[i(1)]
# print(catalog)

# new_cat = zip(*catalog)
# print(new_cat)
# dict_cat = dict(catalog)
# print(dict_cat[1])