class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        print('new car: ', self.name, self.color)

    def go(self):
        print('go')

    def stop(self):
        print('stop')

    def turn(self, direction):
        print('turn', direction)

    def show_speed(self):
        print(f'speed is {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'speed is too big! ({self.speed})')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'speed is too big! ({self.speed})')

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True
        print('This is police!')

car1 = TownCar(50, 'pink', 'Mazda')
car1.go()
car1.turn('left')
car4 = SportCar(100, 'orange', 'Ferrari')
car4.show_speed()
car2 = WorkCar(50, 'green', 'Hundai')
car2.go()
car2.show_speed()
car3 = PoliceCar(70, 'blue', 'Mazda')
car3.show_speed()
car3.stop()