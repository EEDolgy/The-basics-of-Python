my_list = [26, 9, 9, 9, 7, 7, 5, 3, 3, 2, 1, 1, 1, 1]
print(my_list)

while True:
    try:
        n = int(input('Enter a number: '))
    except:
        print('Enter a number')
    else:
        break

if n > my_list[0]:
    my_list.insert(0, n)
else:
    for i in range(len(my_list) - 1,-1,-1):
        if n <= my_list[i]:
            my_list.insert(i + 1, n)
            break

print(my_list)