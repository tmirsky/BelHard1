# Задача 1.
from sqlalchemy import create_engine, MetaData, Table, Integer, Column, String, Float
from sqlalchemy import delete, update, select, insert

meta = MetaData()

engine = create_engine('sqlite:///products.sqlite', echo=True)
conn = engine.connect()

products = Table('products', meta,
                 Column('id', Integer, primary_key=True),
                 Column('name', String),
                 Column('price', Float),
                 Column('amount', Integer),
                 Column('comment', String)
                 )

meta.create_all(engine)


def Insert():
    ins = products.insert().values(
        name=input("Введите название продукта: "),
        price=float(input("Введите цену продукта: ")),
        amount=int(input("Введите количество продукта: ")),
        comment=input("Напишите комментарий: "),
        )
    result = conn.execute(ins)


def View():
    conn = engine.connect()
    select_t = select([products])
    result = conn.execute(select_t)
    print(result.fetchall())


def Delete():
    id = int(input("Введите инвентарный номер продукта для удаления: "))
    deleting = delete(products).where(
        products.c.id.like(id)
    )
    result = conn.execute(deleting)


def Update():
    id = int(input("Enter product id to update: "))
    change = products.update().where(products.c.id.like(id)).values(title=input("Введите новое название продукта: "),
                                                                    price=float(input("Введите новую цену продукта: ")),
                                                                    amount=int(input("Введите количество продукта: ")),
                                                                    comment=input("Напишите комментарий: "))
    result = conn.execute(change)


while True:
    print(
        " 1) для добавления строки в таблицу\n",
        "2) для удаления\n",
        "3) для отображения таблицы\n",
        "4) для обновления данных\n",
        "0) выход\n",
        )

    choice = int(input("Введите номер операции: "))
    if choice == 0:
        break
    else:
        {1: Insert, 2: Delete, 3: View, 4: Update}.get(choice)()


#   Задача 2.
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///vehicles.db', echo=True)
Base = declarative_base()


class Brand(Base):
    __tablename__ = "BRAND"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Car(Base):
    __tablename__ = "CAR"
    id = Column(Integer, primary_key=True)
    model = Column(String)
    release_year = Column(Integer)
    brand = Column(String, ForeignKey('BRAND.name'))
    brand_name = relationship("Brand", back_populates="CAR")


Brand.CAR = relationship("Car", order_by=Car.id, back_populates="brand_name")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def Insert_Brand():
    ins = Brand(name=input("Введите название производителя(брэнд): "))
    session.add(ins)
    session.commit()


def Insert_Car():
    ins = Car(model=input("Введите модель машины: "),
              release_year=int(input("Год выпуска: ")),
              brand=input("Производитель: "))
    session.add(ins)
    session.commit()


def View():
    result1 = session.query(Brand).all()
    for row in result1:
        print("id:", row.id, "Brand:", row.name)
    result2 = session.query(Car).all()
    for row2 in result2:
        print("id:", row2.id, "Model:", row2.model, "Issue year:", row2.release_year, "Brand:", row2.brand)


def Delete_Brand():
    x = session.query(Brand).get(int(input("Enter id to delete: ")))
    session.delete(x)
    session.commit()


def Delete_Car():
    x = session.query(Car).get(int(input("Enter id to delete: ")))
    session.delete(x)
    session.commit()


def Update_Brand():
    x = session.query(Brand).get(int(input("Enter id to update: ")))
    x.name = input("Enter a brand")
    session.commit()


def Update_Car():
    x = session.query(Car).get(int(input("Enter id to update: ")))
    x.model = input("Enter a model")
    x.release_year = int(input("Write a release year: "))
    x.brand = input("Write a brand: ")
    session.commit()


while True:
    print(
        " Введите 1 для внесения данных таблицы brand\n",
        "Введите 2 для внесения данных таблицы car\n",
        "Введите 3 для удаления данных таблицы brand\n",
        "Введите 4 для удаления данных таблицы car\n",
        "Введите 5 для отображения таблицы\n",
        "Введите 6 для обновления данных таблицы brand\n",
        "Введите 7 для обновления данных таблицы car\n",
        "Введите 0 для выхода\n",
    )

    choice = int(input("Введите номер операции: "))
    if choice == 0:
        break
    else:
        {1: Insert_Brand, 2: Insert_Car, 3: Delete_Brand, 4: Delete_Car, 5: View, 6: Update_Brand, 7: Update_Car}.get(
            choice)()