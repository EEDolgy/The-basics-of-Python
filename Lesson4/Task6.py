from itertools import count, cycle

for i in count(7):
    if i > 15:
        break
    print(i)

lst = ['Жил-был царь,', 'у царя был двор,', 'на дворе был кол,', 'на колу мочало;', 'не сказать ли с начала?']

c = 0
for el in cycle(lst):
    if c > 15:
        break
    print(el)
    c += 1