import sqlite3

connection = sqlite3.connect("persons.db")
cursor = connection.cursor()

create_query = 'CREATE TABLE IF NOT EXISTS employees (Name NOT NULL , Surname TEXT,Age INTEGER ,City NOT NULL,' \
               'Salary INTEGER) '

cursor.execute(create_query)

connection.commit()


cities = cursor.execute('SELECT DISTINCT City FROM  employees ').fetchall()

for city in cities:
    avg_salary = cursor.execute(f'SELECT AVG(SALARY) FROM employees WHERE City LIKE "%{city[0]}%"').fetchone()
    print(f'საშუალო ხელფასი, ქალაქში {city[0]} , არის {avg_salary[0]} ლარი')

