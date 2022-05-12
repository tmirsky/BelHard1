# Задача классы сода
addy = input()

class Soda:

    def __init__(self, addy):
        if isinstance(addy, str):
            self.addy = addy
        else:
            self.addy = None

    def show_my_drink(self):
        if self.addy:
            return f'Газировка и {self.addy}'
        else:
            return f'Обычная газировка'

soda = Soda(addy)
print(soda.show_my_drink())

# Задача 1
class Counter:
    def __init__(self, start = 0):
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num

    def increase(self):
        num = self.num
        self.num += 1
        return num

    def decrease(self):
        num = self.num
        self.num -= 1
        return num

count_iter = Counter()
print(count_iter.increase())
print(count_iter.increase())
print(count_iter.increase())
print(count_iter.decrease())
print(count_iter.decrease())
print(count_iter.decrease())
# Задача 2
class Phone:
    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receiveCall(selfs, name):
        name = input()
        return f"Звонит {name}"

    def getinfo(self):
        return [self.brand, self.model, self.issue_year]

    def __str__(self):
        return f'Бренд:{self.brand}, Модель:{self.model},Год выпуска: {self.issue_year}'

p = Phone(input('Введите бренд '),
          input('Введите модель '),
          input('Введите год выпуска ')
              )
print(p.receiveCall(''))
print(p.getinfo())
print(str(p))