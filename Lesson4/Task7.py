from math import factorial

# def fact(n):
#     for el in range(n+1):
#         yield factorial(el)

# def fact(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#         yield res

# for el in fact(5):
#     print(el)

def func(n):
    loc_var = 0
    while True:
        loc_var += 1
        yield loc_var

var = func(4)

print(next(var))
print(next(var))
print(next(var))

print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
