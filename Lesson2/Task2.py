while True:
    try:
        length = int(input('Enter list length: '))
    except:
        print('Number of elements should be integer')
    else:
        if length > 0:
            break
        else:
            print('Number of elements should be > 0')
lst = []
for i in range(length):
    item = int(input('Enter a list element: '))
    lst.append(item)

print(f'The primary list is: {lst}')

for i in range(0, length, 2):
    temp = lst[i]
    try:
        lst[i] = lst[i + 1]
    except IndexError:
        pass
    else:
        lst[i + 1] = temp

print(f'The list after changes: {lst}')