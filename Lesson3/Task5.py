def summ():
    result = 0
    while True:
        num_list = input('Enter numbers or enter Q to quit: ').split()
        for item in num_list:
            if item.upper() == 'Q':
                print(result)
                return
            else:
                result += int(item)
        print(result)

summ()