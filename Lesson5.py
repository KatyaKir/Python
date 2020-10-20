# Задача №1
with open("text_new.txt", 'w', encoding="utf-8") as z1:
    data = 0
    while data != '':
        data = input('Напишите что-нибудь: ')
        if data != '':
            z1.write(data + '\n')
        else:
            z1.close()

# Задача №2
with open("text_new.txt", 'r', encoding="utf-8") as z2:
    line = z2.readlines()
    for ind, el in enumerate(line, 1):
        words = len(el.split())
        print("%d строка состоит из %d слов" % (ind, words))

# Задача №3
with open("text_3.txt", 'r', encoding="utf-8") as z3:
    data = {}
    for el in z3:
        data[el.split()[0]] = float(el.split()[1])
    for empl, money in data.items():
        if money < 20000:
            print("Меньше 20000 зарабатывает:\n %s \n" % empl)
    average = sum(data.values()) / len(data)
    print("Средняя з/п равна: %.2f" % average)

# Задача №4


# Задача №5


# Задача №6
with open("text_6.txt", 'r', encoding="utf-8") as z6:
    for el in z6:
        tab = el.split()
        subject = el.split(':')[0]
        # print(subject)
        for i in tab:
            if '(' in i:
                hours = sum([int(i[:i.index('(')])])
        print({subject: hours})

# Задача №7
import json

with open("text_7.txt", 'r', encoding="utf-8") as z7:
    with open("text_77.json", 'w', encoding="utf-8") as z7_j:
        data = {}
        average = []
        for el in z7:
            name = el.split()[0]
            result = int(el.split()[2]) - int(el.split()[3])
            data = {name: result}
            print(data)
        for i in data.values():
            if i > 0:
                average.append(i)
        av = sum(average) / len(average)
        print("Средняя прибыль равна: %.2f" % av)
        json.dump([data, {'average_profit': av}], z7_j)
