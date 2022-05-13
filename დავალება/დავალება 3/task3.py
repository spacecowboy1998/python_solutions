import sqlite3

connection = sqlite3.connect("census.db")
cursor = connection.cursor()

create_table_query = '''CREATE TABLE IF NOT EXISTS density(province_or_teritory TEXT,
                                                           population INTEGER ,
                                                           land_area REAL)'''

cursor.execute(create_table_query)

# province_file = open("canada.txt", 'r')
# province_list = province_file.readlines()
# province_file.close()
#
# insert_query = '''INSERT INTO density VALUES ('{}',{},{})'''
# for values in province_list:
#     values.rstrip("\n")
#     cursor.execute(insert_query.format(*values.split(",")))

connection.commit()

select_all = '''SELECT * FROM density '''
cursor.execute(select_all)
print("ბაზაში არსებული ყველა მონაცემი: " + "\n", cursor.fetchall())


select_population = '''SELECT population FROM density'''
cursor.execute(select_population)
print("ბაზაში არსებული მოსახლეობის მონაცემები: " + "\n", cursor.fetchall())


select_query = '''SELECT province_or_teritory FROM density WHERE population < 1000000 '''
cursor.execute(select_query)
print("ბაზაში არსებული პროვინციები სადაც მოსახლეობა მილიონზე ნაკლებია:" + "\n", cursor.fetchall())


select_query = '''SELECT province_or_teritory FROM density WHERE population < 1000000 or population > 5000000'''
cursor.execute(select_query)
print("ბაზაში არსებული პროვინციები სადაც მოსახლეობა მილიონზე ნაკლებია და აღემატება 5 მილიონს:" + "\n",
      cursor.fetchall())


select_query = '''SELECT province_or_teritory FROM density WHERE population BETWEEN 1000000 AND 5000000'''
cursor.execute(select_query)
print("ბაზაში არსებული პროვინციები სადაც მოსახლეობა მერყეობს მილიონსა და 5 მილიონს შორის:" + "\n",
      cursor.fetchall())


select_query = 'SELECT population FROM density WHERE land_area > 200000'
cursor.execute(select_query)
print("ბაზაში არსებულ პროვინციათა მოსახლეობა, რომლის ფართბი აღემატება 200000 კმ^2" + "\n", cursor.fetchall())


select_query = '''SELECT province_or_teritory, round(population/land_area,5)  FROM density'''
cursor.execute(select_query)
print("ბაზაში არსებული ტერიტორიები და მათი სიმჭიდროვეები: " + "\n", cursor.fetchall())
