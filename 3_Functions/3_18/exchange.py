def exchange(usd=0, rub=0, rate=0):
    if all([usd, rub, rate]):
        raise ValueError('Too many arguments')
    elif all([usd, rub]) or all([usd, rate]) or all([rub, rate]):
        if all([usd, rub]):
            return rub / usd
        elif all([usd, rate]):
            return usd * rate
        elif all([rub, rate]):
            return rub / rate
    else:
        raise ValueError('Not enough arguments')


print(exchange(rub=1000, rate=85))
