class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки при помощи ручки')

class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки при помощи карандаша')

class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки при помощи маркера')

stat1 = Pen('pen')
stat1.draw()
stat1 = Pencil('pen')
stat1.draw()
stat1 = Handle('pen')
stat1.draw()