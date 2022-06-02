#Задача 1.
from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column

engine = create_engine('sqlite:///products.bd', echo=True)
meta = MetaData()
conn = engine.connect()


products = Table(
        'products', meta,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('price', Integer),
        Column('amount', Integer),
        Column('comment', String)
        )

meta.create_all(engine)


conn.execute(products.insert(),
             [
                 {'name': 'Яблоки', 'price': int(input('Введите стоимость для яблок:')),
               'amount': int(input('Введите количество:'))},
              {'name': 'Бананы', 'price': int(input('Введите стоимость для бананов:')),
               'amount': int(input('Введите количество:'))},
              {'name': 'Персики', 'price': int(input('Введите стоимость для персиков:')),
               'amount': int(input('Введите количество:'))},
              {'name': 'Киви', 'price': int(input('Введите стоимость для киви:')),
               'amount': int(input('Введите количество:'))},
             ])

p_delete = products.delete().where(products.c.id == int(input('Введите номер товара для удаления')))
p_update = products.update().where(products.c.name == 'Киви').values(name='Киви (Эквадор)')

conn.execute(p_delete)
conn.execute(p_update)
# Выполняет запрос на изменение или запускает инструкцию SQL для указанного объекта

picktable = products.select()
conn.execute(picktable).fetchall()
result = conn.execute(picktable)
for i in result:
    print(i)

# var 2
#def Create():
#    ins = product.insert().values(name=input('Введите название товара:'), price=int(input('Введите цену за товар:')),
#                                amount=int(input('Введите количество:')), comment=input('Комментарий:'))
#    result1 = conn.execute(ins)
#    print(f'Добавлена строка')
#
#
#
# def Select():
#     selected = product.select()
#     result2 = conn.execute(selected)
#     for i in result2:
#         print(i)
#
#
# def Update():
#     price_old = int(input('Введите цену:'))
#     price_new = int(input('Введите новую цену:'))
#     upd = product.update().where(product.c.price == price_old).values(price=price_new)
#     result3 = conn.execute(upd)
#     print('Обновление строки')
#
#
# def Delete():
#     delete_name = input('Введите продукт для удаления')
#     deleting = product.delete().where(product.c.name == delete_name)
#     result4 = conn.execute(deleting)
#     print('Удаление')
#
#
#
# while True:
#     choice = int(input(f'Введите номер \n
#     1) для добавления строки в таблицу,\n
#     2) для отображения таблицы,\n
#     3) для изменения данных,\n
#     4) для удаления\nили \n
#     0) выход:'))
#     if choice == 0:
#         break
#     else:
#         {1: Create, 2: Read, 3: Update, 4: Delete}.get(choice)()

#Задача 2.
# from sqlalchemy import create_engine, MetaData, Column, Table, Integer, String, Float
# from sqlalchemy import select, insert, ForeignKey, PrimaryKeyConstraint
# from sqlalchemy.ext.declarative import declarative_base
#
#
#
#
# engine = create_engine('sqlite:///Car.db', echo=True)
# Base = declarative_base()
#
# class Brand(Base):
#     __tablename__ = 'brand'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#
#
# class Car(Base):
#     __tablename__ = 'car'
#
#     model = Column(String)
#     release_year = Column(String)
#     brand = Column(String, ForeignKey('brand.id'))
#in process