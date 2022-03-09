class Employee:
    def __init__(self, name, surname, age, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def print_info(self):
        print(f"დასაქამებულის მონაცებემი სახელი:{self.name}, გვარი:{self.surname},"
              f" შემოსავალი:{self.salary} ლარი , ასაკი:{self.age} წელი")


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

min_salary_person = min(obj_list, key=lambda x: x.salary)
max_age_person = max(obj_list, key=lambda x: x.age)

min_salary_person.print_info()
max_age_person.print_info()
