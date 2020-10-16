with open('fileTask5.txt', 'w+') as f:
    for i in range(1, 30, 3):
        f.write(str(i) + ' ')
    f.seek(0)
    num_list = f.read().split()

num_list = list(map(int, num_list))

print(sum(num_list))