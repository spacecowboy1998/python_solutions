class Employee:
    def __init__(self, name, surname, age, salary):
        self.saxeli = name
        self.gvari = surname
        self.asaki = age
        self.shemosavali = salary


my_file = open("dataset1.csv", "r", encoding="utf8")
my_list = my_file.readlines()
my_file.close()
obj_list = []

for person in my_list:
    person = person.rstrip("\n")
    employee = Employee(
        person.split(",")[0],
        person.split(",")[1],
        int(person.split(",")[2]),
        int(person.split(",")[3])
    )
    obj_list.append(employee)

min_salary_person = min(obj_list, key=lambda x: x.shemosavali)
max_age_person = max(obj_list, key=lambda x: x.asaki)

print(f"მინიმალური ხელფასი არის {min_salary_person.shemosavali} ლარი,იგი ეკუთვნის "
      f"{min_salary_person.saxeli} {min_salary_person.gvari}ს და მისი ასაკია {min_salary_person.asaki} წელი")

print(f"ყველაზე დიდი ასაკი არის {max_age_person.asaki} წელი ,იგი ეკუთვნის "
      f"{max_age_person.saxeli} {max_age_person.gvari}ს და მისი შემოსავალია {max_age_person.asaki} ლარი")
