def while_true(type, condition, request, message='Вы ошиблись, попробуйте еще раз: '):
    while True:
        try:
            result = type(input(request))
        except:
            print(message)
        else:
            if not condition(result):
                print(message)
                continue
            else:
                break
    return result

def pow_1(x, y):
    return x ** y

def pow_2(x, y):
    result = 1
    for i in range(y * (-1)):
        result *= x
    return 1 / result

x = while_true(float, lambda i: i > 0, 'Введите действительное положительное число: ')
y = while_true(int, lambda i: i < 0, 'Введите целое отрицательное число: ')

print(pow_1(x, y))
print(pow_2(x, y))