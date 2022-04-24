age = input('Сколько тебе лет:')
print(f" У нас разница в {abs(int(age)-25)} год/лет")
print(type(age))
print(isinstance(age, str))
print(age is None)
print(bool(age))
print(float(age))
print('Припев песни Eiffel 65 - Blue:\n' + "I'm Blue\n" + 'Da ba dee da ba dye\n' * 7)
surname = input()
name = input()
fio = f'{surname[0]}, {name[0]}'
print(fio)
string = " Mattafix - Big City Life"
print(string[1:9:])
print(len(string))
print(f"{surname:*^20}")
great_evening = ['walkin', 'coffe', 'sweet']
gc = f"Great evening is {', '.join(great_evening)}"
print(gc.find('coffe'))
print(gc.center(70, '*'))