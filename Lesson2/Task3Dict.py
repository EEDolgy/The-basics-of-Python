while True:
    try:
        mnth = int(input('Enter a month number: '))
    except:
        print('Enter a number from 1 to 12')
    else:
        if 1 <= mnth <= 12:
            break
        else:
            print('Enter a number from 1 to 12')

mnth_dict = {
    1: 'winter',
    2: 'winter',
    12: 'winter',
    3: 'spring',
    4: 'spring',
    5: 'spring',
    6: 'summer',
    7: 'summer',
    8: 'summer',
    9: 'autumn',
    10: 'autumn',
    11: 'autumn'
}

print(mnth_dict[mnth])