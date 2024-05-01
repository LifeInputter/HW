class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = int()
        self.buildingType = str()

    def __eq__(self, other):
        if self.numberOfFloors == other and self.buildingType == other:
            return (self.numberOfFloors == other, self.buildingType == other)
            print("Эти дома - одинаковые")

        else:
            print("Дома не похожи")


building_1 = Building(5, "Зима")
building_2 = Building(8, "Зима")

if building_1.__eq__(other=building_2):
    print("В этих домах одинаковое кол-во этажей")
