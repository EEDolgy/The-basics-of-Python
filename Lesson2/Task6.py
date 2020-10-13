prod_list = []

def while_true(type, request, message):
    while True:
        try:
            result = type(input(request))
        except:
            print(message)
        else:
            break
    return result

n = while_true(int, 'Enter number of products: ', 'Number of elements should be integer')

for i in range(n):
    prod_list.append((i, dict()))
    item = input('Enter name: ')
    prod_list[i][1]['name'] = item
    item = while_true(float, 'Enter cost: ', 'Enter a number')
    prod_list[i][1]['cost'] = item
    item = while_true(int, 'Enter quantity: ', 'Enter a number')
    prod_list[i][1]['quantity'] = item
    item = input('Enter units: ')
    prod_list[i][1]['units'] = item

analytics = dict()

for item in prod_list:
    for key, val in item[1].items():
        if key in analytics.keys():
            analytics[key].append(val)
        else:
            analytics[key] = [val]

for key, val in analytics.items():
    print(f'{key}: {val}')

