sec = int(input('Enter seconds: '))

hours = sec // 3600
min = (sec % 3600) // 60
sec = sec - 3600 * hours - 60 * min

print(f'{hours}:{min}:{sec}')