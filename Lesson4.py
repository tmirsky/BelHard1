from num2words import num2words
number1 = float(input('Введите первое число:'))
operation = input('Введите необходимую операцию из перложенных\n' +
                  '(сложение- "+", вычитание - "-", умножение - "*", деление - "/", возведение в степень - "**"):\n')
number2 = float(input('Введите второе число:'))
if operation == '+':
    print(number1 + number2)
    print(num2words((number1 + number2), lang='ru'))
elif operation == '-':
    print(number1 - number2)
    print(num2words((number1 - number2), lang='ru'))
elif operation == '*':
    print(number1 * number2)
    print(num2words((number1 * number2), lang='ru'))
elif operation == '/':
    print(number1 / number2)
    print(num2words((number1 / number2), lang='ru'))
elif operation == '**':
    print(number1 ** number2)
    print(num2words((number1 ** number2), lang='ru'))
else:
    print('Некорректно введены данные')
# Также можно было задать ключи;
# def numtoword(totalnumber)
#     constnum = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
#          6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
#     non_constnum = {10: 'десять', 20: 'двадцать', 30: 'тридцать', 40: 'сорок',
#          50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
#          80: 'восемьдесят', 90: 'девяносто'}
#     non_constnum1 = {11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
#          14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
#          17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}
#    n1 = n % 10
#    n2 = n - n1
#    if n < 10:
#        return constnum.get(n)
#    elif 10 < n < 20:
#        return non_constnum1.get(n)
#    elif n >= 10 and n in non_constnum:
#        return non_constnum.get(n)
#    else:
#        return non_constnum.get(n2) + ' ' + constnum.get(n1)
# но такой алгоритм подходит только для двухзначных чисел int
