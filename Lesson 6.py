# Задача 3.
print('Задание 3:')
lst_a = [11, 2, 5, 6, -7, 4, 3, -2]

def more_than_five(lst_a):
    lst_b = []
    for i in lst_a:
        if abs(i) > 5:
            lst_b.append(i)
    return lst_b

print(more_than_five(lst_a))

# Задача 4.
print('Задание 4:')
a = [7, 12, 17, 30, 45, 53, 64, 75, 139, 21, 34, 55, 89]
for i in a:
    if i != 139 and i % 2 != 0:
        print(i)
    elif i == 139:
        break

# Задача 5.
print('Задание 5:')
lst_rev = list(range(18, 1, -4))
print(lst_rev)
# Задача 6.
print('Задание 6:')
print('Введите число месяцев для определении времени года: ')
month = int(input())
dict_season = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}

def month_to_season(month):
    if month % 12 == 1 or month % 12 == 2 or month % 12 == 0:
        return dict_season[1]
    elif month % 12 == 3 or month % 12 == 4 or month % 12 == 5:
        return dict_season[2]
    elif month % 12 == 6 or month % 12 == 7 or month % 12 == 8:
        return dict_season[3]
    return dict_season[4]

print(f'Сезон:' + month_to_season(month))



#Rename branch