def my_func(a, b, c):
    mn = min(a, b, c)
    if (a, b, c).count(mn) > 1:
        return 'the smallest number is missing'
    else:
        ls = [a, b, c]
        ls.remove(mn)
        return sum(ls)

print(my_func(1, 6, 3))
print(my_func(2, 6, 2))
print(my_func(6, 6, 4))
print(my_func(1, 1, 1))
