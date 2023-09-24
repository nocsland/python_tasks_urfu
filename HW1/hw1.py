# HW1

number = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
number_suf = ['дцать', 'надцать', 'ста', 'сот', 'тысяч']
unique = ['сорок', 'девяносто']

n = input("Введите 5-значное число ")
number_len = len(n)
result = ""
space = " "

if number_len != 5:
    print(f"Было введено {number_len}-значное число")
else:
    a, b, c, d, e = int(n[0]), int(n[1]), int(n[2]), int(n[3]), int(n[4])

# Обработка двух старших разрядов

    # Первая разряд 1, второй не равен 0
    if a == 1 and b == 0:
        result += number[9] + " "
    # Первая разряд 1, второй 1 или 3
    elif a == 1 and b in [1, 3]:
        result += number[b - 1] + number_suf[1] + " "
    # Первая разряд 1, второй 4-9
    elif a == 1 and b in [4, 5, 6, 7, 8, 9]:
        result += number[b - 1][:-1] + number_suf[1] + " "
    # Первый разряд 1, второй 2
    elif a == 1 and b == 2:
        result += number[b - 1][:-1] + "е" + number_suf[1] + " "

    # Первый разряд = 2 или 3, второй = 0
    elif a in [2, 3] and b == 0:
        result += number[a - 1] + number_suf[0] + " "
    # Первый разряд 2 или 3, второй = 1
    elif a in [2, 3] and b == 1:
        result += number[a - 1] + number_suf[0] + " " + number[0][:2] + "на" + " "
    # Первый разряд 2 или 3, второй = 2
    elif a in [2, 3] and b == 2:
        result += number[a - 1] + number_suf[0] + " " + number[1][:-1] + "е" + " "
    # Первый разряд 2 или 3, второй != 1,2
    elif a in [2, 3] and b not in [1, 2]:
        result += number[a - 1] + number_suf[0] + " " + number[b - 1] + " "

    # Первый разряд = 4 и второй = 0
    elif a == 4 and b == 0:
        result += unique[0] + " "
    # Первый разряд = 4 и второй = 1
    elif a == 4 and b == 1:
        result += unique[0] + " " + number[0][:2] + "на" + " "
    # Первый разряд = 4 и второй = 2
    elif a == 4 and b == 2:
        result += unique[0] + " " + number[1][:-1] + "е" + " "
    # Первый разряд = 4 и второй != 1,2
    elif a == 4 and b not in [1, 2]:
        result += unique[0] + " " + number[b - 1] + " "

    # Первый разряд 5-8 и второй != 1,2
    elif a in [5, 6, 7, 8] and b == 0:
        result += number[a - 1] + number[9][:-1] + " "
    # Первый разряд 5-8 и второй = 1
    elif a in [5, 6, 7, 8] and b == 1:
        result += number[a - 1] + number[9][:-1] + " " + number[0][:2] + "на" + " "
    # Первый разряд 5-8 и второй = 2
    elif a in [5, 6, 7, 8] and b == 2:
        result += number[a - 1] + number[9][:-1] + " " + number[1][:-1] + "е" + " "
    # Первый разряд 5-8 и второй = 2
    elif a in [5, 6, 7, 8] and b not in [1, 2]:
        result += number[a - 1] + number[9][:-1] + " " + number[b - 1] + " "

    # Первый разряд = 9 и второй = 0
    elif a == 9 and b == 0:
        result += unique[1] + " "
    # Первый разряд = 9 и второй = 1
    elif a == 9 and b == 1:
        result += unique[1] + " " + number[0][:2] + "на" + " "
    # Первый разряд = 9 и второй = 2
    elif a == 9 and b == 2:
        result += unique[1] + " " + number[1][:-1] + "е" + " "
    # Первый разряд = 9 и второй != 1,2
    elif a == 9 and b not in [1, 2]:
        result += unique[1] + " " + number[b - 1] + " "

    # Добавить "тысяч"
    if a != 1 and b == 1:
        result += number_suf[4] + "а" + " "
    if a != 1 and b in [2, 3, 4]:
        result += number_suf[4] + "и" + " "
    if a == 1 or a != 1 and b in [5, 6, 7, 8, 9, 0]:
        result += number_suf[4] + " "

# Обработка 3-х младших разрядов

    # Обработка сотен
    # Сотни != 0 и = [5-9]
    if c != 0 and c in [5, 6, 7, 8, 9]:
        result += number[c - 1] + number_suf[3] + " "
    # Сотни != 0 и = 1
    elif c != 0 and c == 1:
        result += number_suf[2][:-1] + 'о' + " "
    # Сотни != 0 и = 2
    elif c != 0 and c == 2:
        result += number[1][:-1] + "е" + number_suf[2][:-1] + "и" + " "
    # Сотни != 0 и = [3,4]
    elif c != 0 and c in [3, 4]:
        result += number[c - 1] + number_suf[2] + " "

    # Обработка десятков и единиц
    if d != 0:
        if d != 1 and d in [2, 3]:
            result += number[d - 1] + number_suf[0] + " "
        elif d != 1 and d == 4:
            result += unique[0] + " "
        elif d != 1 and d == 9:
            result += unique[1] + " "
        elif d != 1 and d in [5, 6, 7, 8]:
            result += number[d - 1] + number[9][:-1] + " "
    if e != 0 and d != 1:
        result += number[e - 1]
    elif d == 1 and e == 0:
        result += number[9]
    elif d == 1 and e in [1, 3]:
        result += number[e - 1] + number_suf[1]
    elif d == 1 and e == 2:
        result += number[e - 1][:-1] + "е" + number_suf[1]
    elif d == 1 and e in [4, 5, 6, 7, 8, 9]:
        result += number[e - 1][:-1] + number_suf[1]
print(result.rstrip(" "))
