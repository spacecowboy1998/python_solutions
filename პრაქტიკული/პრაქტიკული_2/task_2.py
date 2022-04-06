import sqlite3
from my_class import Dog

connection = sqlite3.connect("morty.db")
cursor = connection.cursor()

create_query = 'CREATE TABLE IF NOT EXISTS dogs (Name TEXT, Age INTEGER , Color TEXT)'

cursor.execute(create_query)
connection.commit()

dog1 = Dog("Bruno", 15, "Grey")
dog2 = Dog("Alexandra", 5, "Brown")
dog3 = Dog("Batura", 7, "Black")
dog4 = Dog("Loma", 4, "Brown")
dog5 = Dog("Jeka", 12, "Black")

insert_query = 'INSERT INTO dogs VALUES (?,?,?)'
cursor.execute(insert_query, dog1.get_values())
cursor.execute(insert_query, dog2.get_values())
cursor.execute(insert_query, dog3.get_values())
cursor.execute(insert_query, dog4.get_values())
cursor.execute(insert_query, dog5.get_values())
connection.commit()

