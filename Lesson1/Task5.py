proc = int(input('Enter proceeds: '))
costs = int(input('Enter costs: '))

if costs >= proc:
    print('Your financial result is loss =(')
else:
    print('Your financial result is profit =)')
    prof = (proc - costs) / proc
    print(f'Your profitability is {prof}')
    staff = int(input('Enter number of staff: '))
    prof = (proc - costs) / staff
    print(f'Your profit per person is {prof}')