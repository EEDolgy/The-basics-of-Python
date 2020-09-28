a = int(input('Enter the first-day result: '))
b = int(input('Enter the aim result: '))

days = 1

while a < b:
    a *= 1.1
    days += 1

print(f'Sportsmen needs {days} to gain the result of {b}km')