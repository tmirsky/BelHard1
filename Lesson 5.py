from num2words import num2words
print("Простой калькулятор на Python 2.0")
i = 0

while True:
    print('Введите необходимую операцию \n' + '(сложение- "+", вычитание - "-", умножение - "*", деление - "/", возведение в степень - "**"):\n')
    number1 = float(input('Введите число:'))
    operation = input('Действие:')
    number2 = float(input('Введите число:'))

    if operation == '+':
        addition =number1 + number2
        print(addition, (num2words((addition), lang='ru')))
        i = i + 1
    elif operation == '-':
        subtraction = number1 - number2
        print(subtraction, (num2words((subtraction), lang='ru')))
        i = i + 1
    elif operation == '*':
        multiply = number1 * number2
        print(multiply,(num2words((multiply), lang='ru')))
        i = i + 1
    elif operation == '/':
        if number2 != 0:
            division = number1 / number2
            print(division, (num2words((division), lang='ru')))
            i = i + 1
        else:
            print('Ошибка: деление на ноль')
    elif operation == '**':
        power = number1 ** number2
        print(power, (num2words((power), lang='ru')))
        i = i + 1
    else:
        print('Некорректно введены данные')
    if input("Далее/стоп ") == "стоп":
        break
print(f'Количество корректных операций: {i}')