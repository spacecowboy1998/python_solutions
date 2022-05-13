# შექმენით კლასი Triangle. კლასს განუსაზღვრეთ სამი ატრიბუტი -
# სამკუთხედის გვერდები. შეუქმენით მეთოდი area - რომელიც გამოითვლის
# სამკუთხედის ფართობს, ასევე შეუქმენით მეთოდი perimeter - რომელიც
# გამოითვლის პერიმეტრს. შექმენით მეთოდი print_info, რომელიც დაბეჭდავს
# სამკუთხედის გვერდებს, ფართობს და პერიმეტრს. შექმენით Triangle კლასის
# რამდენიმე ობიექტი და აჩვენეთ ფუნქციონალის მუშაობა.


import math


class Triangle:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        semi_perimeter = self.perimeter() / 2
        return math.sqrt(semi_perimeter * (semi_perimeter - self.a) * (semi_perimeter - self.b)
                         * (semi_perimeter - self.c))

    def print_info(self):
        print(f"სამკუთხედის გვერდებია:{self.a},{self.b},{self.c} \n"
              f"მისი პერიმეტრია:{self.perimeter()} \n"
              f"მისი ფართობია:{self.area()}")


triangle = Triangle(4, 5, 6)
print(triangle.perimeter())
print(triangle.area())
triangle.print_info()

triangle2 = Triangle(7, 8, 9)
print(triangle2.perimeter())
print(triangle2.area())
triangle2.print_info()
