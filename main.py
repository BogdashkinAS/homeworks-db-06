import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime


Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.VARCHAR, nullable=False, unique=True)
    publisher_id = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)
    book = relationship(Publisher, backref="book")

class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

class Stok(Base):
    __tablename__ = "stok"

    id = sq.Column(sq.Integer, primary_key=True)
    book_id = sq.Column(sq.Integer, sq.ForeignKey("book.id"))
    shop_id = sq.Column(sq.Integer, sq.ForeignKey("shop.id"))
    count = sq.Column(sq.Integer, nullable=False)

class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, nullable=False)
    data_sale = sq.Column(sq.Date, nullable=False)
    stok_id = sq.Column(sq.Integer, sq.ForeignKey("stok.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)
    sale = relationship(Stok, backref="book")

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def create_info_tables():
    pb1 = Publisher(name="Пушкин")
    pb2 = Publisher(name="Есенин")
    pb3 = Publisher(name="Маяковский")
    pb4 = Publisher(name="Лермонтов")
    pb5 = Publisher(name="Тютчев")

    session.add_all([pb1, pb2, pb3, pb4, pb5])
    session.commit()  

    bk1 = Book(title="Капитанская дочка", book=pb1)
    bk2 = Book(title="Руслан и Людмила", book=pb1)
    bk3 = Book(title="Евгений Онегин", book=pb1)
    bk4 = Book(title="Дубровский", book=pb1)
    bk5 = Book(title="Станционный смотритель", book=pb1)

    session.add_all([bk1, bk2, bk3, bk4, bk5])
    session.commit()  

    bk1 = Book(title="Анна Снегина", book=pb2)
    bk2 = Book(title="Белая береза", book=pb2)
    bk3 = Book(title="Бельгия", book=pb2)
    bk4 = Book(title="Богатырский посвист", book=pb2)
    bk5 = Book(title="Воспоминание", book=pb2)

    session.add_all([bk1, bk2, bk3, bk4, bk5])
    session.commit()  

    bk1 = Book(title="Облако в штанах", book=pb3)
    bk2 = Book(title="Баня", book=pb3)
    bk3 = Book(title="Взял", book=pb3)
    bk4 = Book(title="Рыкающий парнас", book=pb3)
    bk5 = Book(title="Требник троих", book=pb3)

    session.add_all([bk1, bk2, bk3, bk4, bk5])
    session.commit()  

    bk1 = Book(title="Мцыри", book=pb4)
    bk2 = Book(title="Герой нашего времени", book=pb4)
    bk3 = Book(title="Демон", book=pb4)
    bk4 = Book(title="Маскарад", book=pb4)
    bk5 = Book(title="Штосс", book=pb4)

    session.add_all([bk1, bk2, bk3, bk4, bk5])
    session.commit()  

    bk1 = Book(title="Весенние воды", book=pb5)
    bk2 = Book(title="Весенняя гроза", book=pb5)
    bk3 = Book(title="Весна", book=pb5)
    bk4 = Book(title="Два единства", book=pb5)
    bk5 = Book(title="День и ночь", book=pb5)

    session.add_all([bk1, bk2, bk3, bk4, bk5])
    session.commit()  

    sp1 = Shop(name="Калейдоскоп")
    sp2 = Shop(name="Мир знаний")
    sp3 = Shop(name="Дом книги")
    sp4 = Shop(name="Знание")
    sp5 = Shop(name="Книга")

    session.add_all([sp1, sp2, sp3, sp4, sp5])
    session.commit()  

    sk1 = Stok(book_id = 1, shop_id = 1, count = 5)
    sk2 = Stok(book_id = 2, shop_id = 2, count = 5)
    sk3 = Stok(book_id = 3, shop_id = 3, count = 5)
    sk4 = Stok(book_id = 4, shop_id = 4, count = 5)
    sk5 = Stok(book_id = 5, shop_id = 5, count = 5)
    sk6 = Stok(book_id = 6, shop_id = 5, count = 5)
    sk7 = Stok(book_id = 7, shop_id = 4, count = 5)
    sk8 = Stok(book_id = 8, shop_id = 3, count = 5)
    sk9 = Stok(book_id = 9, shop_id = 2, count = 5)
    sk10 = Stok(book_id = 10, shop_id = 1, count = 5)
    sk11 = Stok(book_id = 11, shop_id = 1, count = 5)
    sk12 = Stok(book_id = 12, shop_id = 2, count = 5)
    sk13 = Stok(book_id = 13, shop_id = 3, count = 5)
    sk14 = Stok(book_id = 14, shop_id = 4, count = 5)
    sk15 = Stok(book_id = 15, shop_id = 5, count = 5)
    sk16 = Stok(book_id = 16, shop_id = 5, count = 5)
    sk17 = Stok(book_id = 17, shop_id = 4, count = 5)
    sk18 = Stok(book_id = 18, shop_id = 3, count = 5)
    sk19 = Stok(book_id = 19, shop_id = 2, count = 5)
    sk20 = Stok(book_id = 20, shop_id = 1, count = 5)
    sk21 = Stok(book_id = 21, shop_id = 1, count = 5)
    sk22 = Stok(book_id = 22, shop_id = 2, count = 5)
    sk23 = Stok(book_id = 23, shop_id = 3, count = 5)
    sk24 = Stok(book_id = 24, shop_id = 4, count = 5)
    sk25 = Stok(book_id = 25, shop_id = 5, count = 5)
    session.add_all([sk1, sk2, sk3, sk4, sk5, sk6, sk7, sk8, sk9, sk10, sk11, sk12, sk13, sk14, sk15, sk16, sk17, sk18, sk19, sk20, sk21, sk22, sk23, sk24, sk25])
    session.commit()  

    se1 = Sale(price = 100, data_sale = '2001-01-01', stok_id = 1, count = 5)
    se2 = Sale(price = 200, data_sale = '2002-02-02', stok_id = 2, count = 5)
    se3 = Sale(price = 300, data_sale = '2003-03-03', stok_id = 3, count = 5)
    se4 = Sale(price = 400, data_sale = '2004-04-04', stok_id = 4, count = 5)
    se5 = Sale(price = 500, data_sale = '2005-05-05', stok_id = 5, count = 5)
    se6 = Sale(price = 600, data_sale = '2006-06-06', stok_id = 6, count = 5)
    se7 = Sale(price = 700, data_sale = '2007-07-07', stok_id = 7, count = 5)
    se8 = Sale(price = 800, data_sale = '2008-08-08', stok_id = 8, count = 5)
    se9 = Sale(price = 900, data_sale = '2009-09-09', stok_id = 9, count = 5)
    se10 = Sale(price = 1000, data_sale = '2010-10-10', stok_id = 10, count = 5)
    se11 = Sale(price = 1100, data_sale = '2011-11-11', stok_id = 11, count = 5)
    se12 = Sale(price = 1200, data_sale = '2012-12-12', stok_id = 12, count = 5)
    se13 = Sale(price = 1300, data_sale = '2013-01-13', stok_id = 13, count = 5)
    se14 = Sale(price = 1400, data_sale = '2014-02-14', stok_id = 14, count = 5)
    se15 = Sale(price = 1500, data_sale = '2015-03-15', stok_id = 15, count = 5)
    se16 = Sale(price = 1600, data_sale = '2016-04-16', stok_id = 16, count = 5)
    se17 = Sale(price = 1700, data_sale = '2017-05-17', stok_id = 17, count = 5)
    se18 = Sale(price = 1800, data_sale = '2018-06-18', stok_id = 18, count = 5)
    se19 = Sale(price = 1900, data_sale = '2019-07-19', stok_id = 19, count = 5)
    se20 = Sale(price = 2000, data_sale = '2020-08-20', stok_id = 20, count = 5)
    se21 = Sale(price = 2100, data_sale = '2021-09-21', stok_id = 21, count = 5)
    se22 = Sale(price = 2200, data_sale = '2022-10-22', stok_id = 22, count = 5)
    se23 = Sale(price = 2300, data_sale = '2021-11-21', stok_id = 23, count = 5)
    se24 = Sale(price = 2400, data_sale = '2020-09-20', stok_id = 24, count = 5)
    se25 = Sale(price = 2500, data_sale = '2019-08-19', stok_id = 25, count = 5)
    session.add_all([se1, se2, se3, se4, se5, se6, se7, se8, se9, se10, se11, se12, se13, se14, se15, se16, se17, se18, se19, se20, se21, se22, se23, se24, se25])
    session.commit()  

def list_author():
    name_list = []
    s = session.query(Publisher.name).all()
    for i in s:
        name_list.append(*i)
    return name_list

def author():
    name = input('Введите автора (Пушкин, Есенин, Маяковский, Лермонтов, Тютчев: ): ')
    print()
    name_list = list_author()
    if name in name_list:
        q = session.query(Book.title, Shop.name, Sale.price, Sale.data_sale).select_from(Publisher).join(Book).join(Stok).join(Shop).join(Sale).filter(Publisher.name == name).all()
        for i in q:
            str1 = str(i.data_sale)
            date = datetime.strptime(str1, '%Y-%m-%d').strftime('%d-%m-%Y')
            print(f'{i.title} | {i.name} | {i.price} | {date}')
    else:
        print('Такого автора не существует!')

if __name__ == '__main__':

    BD = ''
    login = ''
    password = ''
    host = ''
    port = ''
    base = ''

    DSN = (f'{BD}://{login}:{password}@{host}:{port}/{base}')

    engine = sqlalchemy.create_engine(DSN)

    Session = sessionmaker(bind=engine)
    session = Session()

    create_tables(engine)
    create_info_tables()
    author()
    session.close()