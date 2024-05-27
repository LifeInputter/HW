def add_everything_up(a, b):
    try:
        return a + b

    except TypeError:
        print(a, b)


result = add_everything_up(3, 3.142)
print(round(result, 2))

result = add_everything_up('Цветок', 2)
print(result)

result = add_everything_up("сущность", [5, 10, 12])
print(result)

result = add_everything_up(1, -5)
print(result)

result = add_everything_up("сияние", 'Небосклон')
print(result)
