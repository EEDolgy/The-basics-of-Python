class Worker:
    def __init__(self, name, surname, position, wage):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": 5000}

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self._income.values())

worker1 = Position('Anna', 'Ivanova', 'HR', 10000)
print(worker1.get_full_name())
print(worker1.get_total_income())