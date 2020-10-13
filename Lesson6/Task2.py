class Road:
    __kg = 25
    __sm = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        print(self._width * self._length * Road.__kg * Road.__sm / 1000)

road = Road(5000, 20)
road.mass()