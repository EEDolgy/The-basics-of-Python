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

mnth_list = ['winter', 'spring', 'summer', 'autumn']

if mnth < 3 or mnth == 12:
    print(mnth_list[0])
elif 2 < mnth < 6:
    print(mnth_list[1])
elif 5 < mnth < 9:
    print(mnth_list[2])
else:
    print(mnth_list[3])