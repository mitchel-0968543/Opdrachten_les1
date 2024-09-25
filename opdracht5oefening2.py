numbers = list(range(1, 100))
for number in numbers:
    priemgetal = True
    for deler in numbers:
        if number > deler > 1:
            if number % deler == 0:
                priemgetal = False
                break
    if priemgetal:
        print(number)