# Задача №1
def a_per_m(a, m):
    global apple, men
    apple = int(input("Сколько яблок делим?"))
    men = int(input("На сколько человек?"))
    try:
        a_per_m = a // m
        if a % m != 0:
            print("Каждому достанется по %d яблок и дольке" % a_per_m)
        else:
            print("Каждому достанется по %d яблок" % a_per_m)
    except NameError:
        print("Введите число!")
    except ZeroDivisionError:
        print("Так и есть их не кому!")
    return


print(a_per_m(apple, men))


# Задача №2
def user(n, s, ye, c, e, p):
    global name, surname, year, city, email, phone, book
    name = input('Введите имя')
    surname = input('Введите фамилию')
    year = input('Год рождения')
    city = input('Город')
    email = input('Ваш email')
    phone = input('Телефон')
    return {'Имя': n, "Фамилия": s, 'Год рождения': ye, 'Город': c, 'email': e, 'телефон': p}


book = user(n=name, s=surname, ye=year, c=city, e=email, p=phone)
print('Имя: {Имя:s}; Фамилия: {Фамилия:s}; Год рождения: {Год рождения:s}; Город: {Город:s}; email: {email:s}; '
      'телефон: {телефон:s}'.format(**book))


# Задача №3
def my_func(n1, n2, n3):
    orange = [n1, n2, n3]
    orange.remove(min(orange))
    return sum(orange)


print(my_func(10, 20, 12))


# Задача №4
def ft():
    global x, y
    x = float(input('Введите действительное положительное число:'))
    y = int(input('Введите целое отрицательное число:'))
    return x ** (1 / abs(y))


val_xy = round(ft(), 4)
print(val_xy)


# Задача №5
n = []
while True:
    numbers = input('Введите какие-то цифры через пробел (для выхода наберите "q"):')
    list_of_numbers = numbers.split()
    if 'q' not in list_of_numbers:
        int_lst = [int(x) for x in list_of_numbers]
        summa = sum(int_lst)
        print(summa)
        n.append(summa)
        print(sum(n))
    elif 'q' in list_of_numbers:
        list_of_numbers.remove('q')
        int_lst = [int(x) for x in list_of_numbers]
        summa = sum(int_lst)
        print(summa)
        n.append(summa)
        print(sum(n))
        break
    else:
        print('Что-то опять пошло не так')


# Задача №6
def int_func():
    words = input('Введите какие-то очень важные слова:')
    list_of_words = words.split()
    letter = 1040
    while letter < 1104:
        for word in list_of_words:
            if chr(letter) in word:
                list_of_words.remove(word)
        letter += 1
    return list(map(str.title, list_of_words))


asrd = int_func()
print(asrd)
