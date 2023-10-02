# HW1 v2


def num_to_words(n):
    number = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
    number_suf = ['дцать', 'надцать', 'ста', 'сот', 'тысяч']
    unique = ['сорок', 'девяносто']
    n = str(n)
    # n = input("Введите 5-значное число ")
    number_len = len(n)
    result = ""

    if number_len != 5:
        return f"Было введено {number_len}-значное число"
    else:
        a, b, c, d, e = map(int, n)

        # Обработка двух старших разрядов
        if a == 1:
            result += number[9] + " " if b == 0 else (
                number[b - 1] + number_suf[1] + " " if b in [1, 3] else
                number[b - 1][:-1] + number_suf[1] + " " if b in [4, 5, 6, 7, 8, 9] else
                number[b - 1][:-1] + "е" + number_suf[1] + " " if b == 2 else "")
        elif a in [2, 3]:
            result += (number[a - 1] + number_suf[0] + " " if b == 0 else
                       number[a - 1] + number_suf[0] + " " + number[0][:2] + "на" + " " if b == 1 else
                       number[a - 1] + number_suf[0] + " " + number[1][:-1] + "е" + " " if b == 2 else
                       number[a - 1] + number_suf[0] + " " + number[b - 1] + " " if b not in [1, 2] else "")
        elif a == 4:
            result += (unique[0] + " " if b == 0 else
                       unique[0] + " " + number[0][:2] + "на" + " " if b == 1 else
                       unique[0] + " " + number[1][:-1] + "е" + " " if b == 2 else
                       unique[0] + " " + number[b - 1] + " " if b not in [1, 2] else "")
        elif a in [5, 6, 7, 8]:
            result += (number[a - 1] + number[9][:-1] + " " if b == 0 else
                       number[a - 1] + number[9][:-1] + " " + number[0][:2] + "на" + " " if b == 1 else
                       number[a - 1] + number[9][:-1] + " " + number[1][:-1] + "е" + " " if b == 2 else
                       number[a - 1] + number[9][:-1] + " " + number[b - 1] + " " if b not in [1, 2] else "")
        elif a == 9:
            result += (unique[1] + " " if b == 0 else
                       unique[1] + " " + number[0][:2] + "на" + " " if b == 1 else
                       unique[1] + " " + number[1][:-1] + "е" + " " if b == 2 else
                       unique[1] + " " + number[b - 1] + " " if b not in [1, 2] else "")

        # Добавить "тысяч"
        if a != 1 and b == 1:
            result += number_suf[4] + "а" + " "
        if a != 1 and b in [2, 3, 4]:
            result += number_suf[4] + "и" + " "
        if a == 1 or a != 1 and b in [5, 6, 7, 8, 9, 0]:
            result += number_suf[4] + " "

        # Обработка 3-х младших разрядов
        if c != 0:
            result += (number[c - 1] + number_suf[3] + " " if c in [5, 6, 7, 8, 9] else
                       number_suf[2][:-1] + 'о' + " " if c == 1 else
                       number[1][:-1] + "е" + number_suf[2][:-1] + "и" + " " if c == 2 else
                       number[c - 1] + number_suf[2] + " ")
        if d != 0:
            result += (number[d - 1] + number_suf[0] + " " if d != 1 and d in [2, 3] else
                       unique[0] + " " if d == 4 else
                       unique[1] + " " if d == 9 else
                       number[d - 1] + number[9][:-1] + " " if d in [5, 6, 7, 8] else "")
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

        return result.rstrip(" ")
