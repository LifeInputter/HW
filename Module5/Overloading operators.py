class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


building_1 = Building(3, "Зима")
building_2 = Building(5, "Зима")

print(building_1 != building_2)

if building_1.__eq__(building_2):
    print("Эти дома похожи")
else:
    print("Дома разного типа")
