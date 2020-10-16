sttr = input('Enter some sentence: ')

lst = sttr.split()

for i in range(len(lst)):
    lst[i] = lst[i][:10] if len(lst[i]) > 10 else lst[i] #можно было без if
    print(i, lst[i])