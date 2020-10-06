from functools import reduce

lst = [el for el in range(100, 1001, 2)]

result = reduce(lambda x, y: x * y, lst)

print(result)