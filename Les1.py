# Задача №1
que1 = input("Привет! Как тебя зовут?")
que2 = input("Рада знакомству, %s! Сколько тебе лет?" % que1)
print("Наш пользователь: %s, %s лет" % (que1, que2))

# Задача №2
sec = int(input("Введите количество секунд:"))
hh = sec // 3600
mm = sec % 3600 // 60
ss = sec % 3600 % 60
print('Время: %02d:%02d:%02d' % (hh, mm, ss))

# Задача №3
d1 = input("Введите любое целое число:")
d = int(d1) + int(d1 + d1) + int(d1 + d1 + d1)
print(d)

# Задача №4
number = int(input("Введите целое положительное число:"))
r = -1
while number > 10:
    tail = number % 10
    number //= 10
    if tail > r:
        r = tail
print(r)

# Задача №5
revenue = int(input("Выручка комапнии:"))
costs = int(input("Издержки компании:"))
fin_res = revenue - costs
if fin_res < 0:
    print("Убыток")
else:
    prof = fin_res / revenue * 100
    print("Рентабельность: %d %%" % prof)
    personal = int(input("Укажите количество сотрудников:"))
    ppp = fin_res / personal
    print("Прибыль на одного сотрудника: %.1f" % ppp)

# Задача №6
km = int(input("Эй, спорсмен, сколько километров ты пробежал сегодня?"))
km_dream = int(input("Сколько км ты мечтаешь пробежать?"))
day = 1
if km == 0:
    print("Тебе никогда не стать марафонцем…")
else:
    while km < km_dream:
        print('День %d: спортсмен пробежал %.1f км' % (day, km))
        km = km * 1.1
        day = day + 1
    print('Спортсмен пробежит дистанцию своей мечты через %d дней' % day)
