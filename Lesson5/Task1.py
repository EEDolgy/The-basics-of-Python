with open('fileTask1.txt', 'w') as f:
    while True:
        text = input('Enter some data or press Enter to exit: ')
        if text == '':
            break
        f.writelines(text + '\n')
