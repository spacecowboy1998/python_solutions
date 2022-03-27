class Book:
    def __init__(self, name, author, year, pages):
        self.__name = name
        self.__author = author
        self.__year = year
        self.__pages = pages

    def info(self):
        print(f"წიგნის სახელია {self.__name} , იგი დაიბეჭდა {self.__year} წელს,"
              f" მისი ავტორია {self.__author} და იგი შედგება {self.__pages} გვერდისგან")

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        print(self.__name)

    def get_year(self):
        return self.__year

    def __eq__(self, other):
        return self.__year == other.get_year()


book1 = Book("კაცია-ადამიანი?", "ილია ჭავჭავაძე", 1858, 1231)
book2 = Book("ვეფხისტყაოსანი", "შოთა რუსთაველი", 1712, 2022)
book3 = Book("ალუდა ქეთელაური", "ვაჟა-ფშაველა", 1888, 762)
book4 = Book("გამზრდელი", "აკაკი წერეთელი", 1898, 252)

book1.info()

print("\n")
book2.get_name()
book2.set_name("სასიყვარულო პოემა თამარს")
book2.get_name()
book2.info()

print("\n ")

print(f"მოსაზრება რომ ალუდა ქეთელაურისა და გაზრდელის დაბეჭდვის დარიღი "
      f"ერთმანეთს ემთხვევა არის: {book3.get_year() == book4.get_year()}")
