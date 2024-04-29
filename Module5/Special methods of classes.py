class House:

    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)



My_house = House()
My_house.setNewNumberOfFloors(5)
