from num2words import num2words
print("Простой калькулятор на Python 2.0")
i = 0
while True:
    print('Введите необходимую операцию \n' + '(сложение- "+", вычитание - "-", умножение - "*", деление - "/", возведение в степень - "**"):\n')
    number1 = float(input('Введите число:'))
    operation = input('Действие:')
    number2 = float(input('Введите число:'))

    if operation == '+':
        print(number1 + number2)
        print(num2words((number1 + number2), lang='ru'))
        i = i + 1
    elif operation == '-':
        print(number1 - number2)
        print(num2words((number1 - number2), lang='ru'))
        i = i + 1
    elif operation == '*':
        print(number1 * number2)
        print(num2words((number1 * number2), lang='ru'))
        i = i + 1
    elif operation == '/':
        if number2 != 0:
            print(number1 / number2)
            print(num2words((number1 / number2), lang='ru'))
            i = i + 1
        else:
            print('Ошибка: деление на ноль')
    elif operation == '**':
        print(number1 ** number2)
        print(num2words((number1 ** number2), lang='ru'))
        i = i + 1
    else:
        print('Некорректно введены данные')
    if input("Далее/стоп ") == "стоп":
        break
print(f'Количество корректных операций: {i}')