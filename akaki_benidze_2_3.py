# შექმენით კლასი Animal. კლასს შეუქმენით ატრიბუტი: სახელი. შექმენით
# კლასი Dog, რომელიც იქნება Animal კლასის მემკვიდრე. Dog კლასს
# განუსაზღვრეთ ატრიბუტები: ასაკი, ფერი. ორივე კლასს შეუქმენით მეთოდი
# info(), რომელიც დაბეჭდავს ინფორმაციას კლასზე. დაიცავით ენკაფსულაციის
# პრინციპი. კლასებს შეუქმენით გეთერები და სეთერები. შექმენით Dog
# კლასის რამდენიმე ობიექტი და აჩვენეთ ფუნქციონალის მუშაობა.


class Animal:

    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self._name = name

    def info(self):
        print(f"ცხოვრელის სახელია {self._name}")

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


class Dog(Animal):

    def __init__(self, age, color, **kwargs):
        super().__init__(**kwargs)
        self._age = age
        self._color = color

    def info(self):
        print(f"ძაღლის სახელია {self._name},მისი ასაკია {self._age},მისი ფერია {self._color}")

    def get_age(self):
        return self._age

    def get_color(self):
        return self._color

    def get_name(self):
        return self._name

    def set_color(self, color):
        self._color = color

    def set_age(self, age):
        self._age = age

    def set_name(self, name):
        self._name = name


bruno = Dog(name="bruno", age=8, color="black")

bruno.info()
print(bruno.get_name())
bruno.set_name("aleksandra")
bruno.info()

jeka = Dog(name="jeka", age=2, color='brown')
jeka.info()
print(jeka.get_age())
jeka.set_age(5)
jeka.info()
