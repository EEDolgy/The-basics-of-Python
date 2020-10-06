def division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "You can't divide by 0!"

a = int(input('Enter dividend: '))
b = int(input('Enter divider: '))

print(division(a, b))
