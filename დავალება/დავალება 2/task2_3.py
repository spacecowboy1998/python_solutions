class Animal:

    def __init__(self, name, age, **kwargs):
        super().__init__(**kwargs)
        self._name = name
        self._age = age

    def info(self):
        print(f"ცხოვრელის სახელია {self._name} და მისი ასაკია {self._age}")


class Dog(Animal):

    def __init__(self, breed, color, **kwargs):
        super().__init__(**kwargs)
        self._breed = breed
        self._color = color

    def info(self):
        print(f"ცხოვრელის სახელია {self._name}, ის არის {self._age} წლის, "
              f"მისი ჯიშია {self._breed} და მისი ფერია {self._color} ")


test_animal = Animal("ბათურა", 15)
test_animal.info()

test_dog2 = Dog(name="ლომა", age=7, breed="კავკასიური ნაგაზი", color="თეთრი")
test_dog2.info()
