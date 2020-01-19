class car:
    def __init__(self):
        self.__update()
    def drive(self):
        print('driving')
    def __update(self):
        print("updating")

bcar=car()
bcar.drive()
