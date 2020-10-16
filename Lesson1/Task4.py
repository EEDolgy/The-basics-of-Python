num = int(input('Enter a number: '))

max = num % 10
i = 1
j = 10

while num // j != 0 :
    current_num = (num % j) // i
    if current_num > max:
        max = current_num
    i *= 10
    j *= 10

current_num = num // i
if current_num > max:
    max = current_num
print(f'max = {max}')