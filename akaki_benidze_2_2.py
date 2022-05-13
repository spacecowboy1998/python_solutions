# შექმენით კლასი Student. განუსაზღვრეთ ატრიბუტები: სახელი, ასაკი,
# უნივერსიტეტი და gpa. კლასისთვის გადატვირთეთ ნაკლებობის და
# მეტობის ოპერატორები. შედარება უნდა მოხდეს gpa ატრიბუტით. კლასს
# ასევე გადაუტვირთეთ სტრიქონდა წარმოდგენის ოპერატორი. შექმენით
# Student კლასის სამი ობიექტი. დაადგინეთ სამეულში მაქსიმალური gpa-ს
# მქონე სტუდენტი და დაბეჭდეთ ეკრანზე.
class Student:

    def __init__(self, name, age, university, gpa):
        self.name = name
        self.age = age
        self.university = university
        self.gpa = gpa

    def __lt__(self, other):
        return self.gpa < other.gpa

    def __gt__(self, other):
        return self.gpa > other.gpa

    def __str__(self):
         return f"{self.name} {self.age} {self.university} {self.gpa}"


student1 = Student("ლუკა", 18, "BTU", 2.1)
student2 = Student("ნიკა", 19, "BTU", 3.8)
student3 = Student("ალეკო", 18, "BTU", 4.0)

max_gpa_person = max([student1, student2, student3])
print(f"მაქსიმალური gpa მქონე სტუდენტი არის: {max_gpa_person.name}\n"
      f"მისი gpa არის: {max_gpa_person.gpa}")

print(str(student1))
