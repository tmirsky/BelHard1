# Задание 8.
lst_a = [11, 2, 5, 6, -7, 4, 3, -2]

def decorator(sad):
    def wrapper(arg):
        lst_b = []
        for i in lst_a:
            if i % 2 == 0:
                lst_b.append(i)
        return lst_b
    return wrapper

@decorator
def more_dev2():
    return lst_a

print(more_dev2(lst_a))

print()
# Задание 9.
class Car:

    __brand = "Tesla"
    __model = "Model 3"
    __year = 2020
    __speed = 0

    def __init__(self):
        print("Двигатель заведен")


    def speed_up(self):
        Car.__speed = 0
        up = Car.__speed
        up += 5
        return f'Нажали на кнопку увеличение скорости - скорость {up}'

    def speed_down(self):
        Car.__speed = 0
        down = Car.__speed
        down -= 5
        return f'Нажали на кнопку уменьшения скорости - скорость {down}'

    def stop_car(self):
        Car.__speed = 0
        stop = Car.__speed
        stop = 0
        return f'Нажали на кнопку Стоп - скорость {stop}'

    def reversal_car(self):
        Car.__speed = 0
        reversal = Car.__speed*-1
        return f'Нажали на кнопку разворот - скорость {reversal}'

car_a = Car()
print(car_a.speed_up())
print(car_a.speed_down())
print(car_a.stop_car())
print(car_a.reversal_car())

print()
#Задание 10.
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        self.__year = 1967

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year != 1967:
            print("Только 1967 год!")
        else:
            self.__year = year

    @property
    def carbrand(self):
        return self.__brand

    @property
    def carmodel(self):
        return self.__model

    def display_info(self):
        print(f" Информация о машине: {self.__brand} {self.__model} ({self.__year} года выпуска)")


car = Car("Chevrolet", "Impala")
print(f"Информация по состоянию на 2025 год:")
car.display_info()
print()
class CarOwner:
    def __init__(self, first_name, second_name):
        self.__first_name = first_name
        self.__second_name = second_name
        self.__age = 18

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 18 < age < 75:
            self.__age = age
        else:
            print("Недопустимый возраст для владельца машины")

    @property
    def firstname(self):
        return self.__first_name

    @property
    def secondname(self):
        return self.__second_name

    def display_info(self):
        print(f" Имя владельца машины: {self.__first_name}\n"
              f" Фамилия владельца машины: {self.__second_name}\n"
              f" Возраст владельца машины: {self.__age}")


dean = CarOwner("Dean", "Winchester")
dean.age = 46
print(f"Информация по состоянию на 2025 год:")
dean.display_info()