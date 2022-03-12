class CallMixin:

    def call(self):
        print(f"ზარის ადრესატია {self.first_name} {self.last_name},"
              f"რომლის ტელეფონის ნომერია {self.phone}")


class Person(CallMixin):

    def __init__(self, first_name, last_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def info(self):
        print(f"პირვნების სახელი და გვარია {self.first_name} {self.last_name},"
              f"მისი ტელეფონის ნომერია {self.phone}")


person = Person("akaki", "benidze", 595508618)

person.info()
person.call()
