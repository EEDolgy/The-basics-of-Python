from math import factorial

def fact(n):
    for el in range(n+1):
        yield factorial(el)

for el in fact(5):
    print(el)