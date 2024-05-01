class Building:
    total = 0

    def __init__(self):
        Building.total += 1


# В цикле создайте 40 объектов класса Building и выведите их на экран командой print

building_quantity = []
max_quantity = 40
while len(building_quantity) < max_quantity:
    new_building = Building()
    building_quantity.append(new_building)
print(Building.total)

# Вариант решения с циклом for:

print("***Вывод в цикле for:***")
building_quantity = []
max_quantity = 40
for i in range(1, max_quantity + 1):  # 1 добавлена, чтобы вывести в консоль 1-40, а не 0-39
    if len(building_quantity) < max_quantity:
        new_building = Building()
        building_quantity.append(new_building)
    print(i)
