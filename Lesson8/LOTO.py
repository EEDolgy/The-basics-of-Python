import random

class Card:
    num_list = [el for el in range(1, 91)]

    def __init__(self, name):
        self.name = name
        self.data = [Card.add_spaces(Card.form_line()) for _ in range(3)]

    @classmethod
    def form_line(cls):
            numbers = cls.num_list.copy()
            line = []
            for i in range(5):
                var = numbers[:i-4] if i < 4 else numbers
                num = random.choice(var)
                line.append(num)
                numbers = [el for el in numbers if el > num]
            for el in line:
                cls.num_list.remove(el)
            return line

    @staticmethod
    def add_spaces(lst):
        places = [el for el in range(9)]
        for i in range(4):
                var = places[:i-3] if i < 3 else places
                place = random.choice(var)
                lst.insert(place, ' ')
                places = [el for el in places if el > place]
        return lst

    def __str__(self):
        result = 'Карточка ' + self.name + '\n'
        result += '-' * 22 + '\n'
        result += '\n'.join(' '.join(map(str, el)) for el in self.data) + '\n'
        result += '-' * 22
        return result

    def contains(self, item):
        for line in self.data:
            result = True if item in line else False
            if result:
                return True
        return False

    def is_empty(self):
        for line in self.data:
            for item in line:
                if type(item) == int:
                    return False
        return True

    def delete(self, num):
        for line in self.data:
            for i, item in enumerate(line):
                if item == num:
                    line[i] = '-'
                    break

class Game:
    num_list = [el for el in range(1, 91)]

    def __init__(self, player1, player2):
        self.card1 = Card(player1)
        self.card2 = Card(player2)
        self.turn = 1
        self.num_count = len(Game.num_list)

    def __str__(self):
        result = '\n' + f'Новый бочонок: {self.current_barrel} (осталось {self.num_count})\n'
        result += str(self.card1) + '\n' + str(self.card2)
        return result

    def new_barrel(self):
        self.current_barrel = random.choice(Game.num_list)
        self.num_count -= 1
        Game.num_list.remove(self.current_barrel)

    def choice(self, answ):
        answ = answ.lower()
        if answ == 'y':
            if self.card1.contains(self.current_barrel):
                self.card1.delete(self.current_barrel)
                return True
            else:
                return False
        elif answ == 'n':
            if self.card1.contains(self.current_barrel):
                return False
            else:
                return True

    def computer_choice(self):
        mistake = random.randint(0, 100)
        if self.card2.contains(self.current_barrel) and mistake >= 2:
                self.card2.delete(self.current_barrel)

game = Game('Human', 'Computer')
while True:
    game.new_barrel()
    print(game)
    answ = input('Зачеркнуть цифру? (y/n)')
    game.computer_choice()
    result = game.choice(answ)
    if not result:
        print('Вы проиграли, компьютер победил!')
        break
    if game.card1.is_empty() and not game.card2.is_empty():
        print('Вы обедили, компьютер проиграл!')
        break
    elif not game.card1.is_empty() and game.card2.is_empty():
        print('Вы проиграли, компьютер победил!')
        break
    elif game.card1.is_empty() and game.card2.is_empty():
        print('Ничья!')
        break