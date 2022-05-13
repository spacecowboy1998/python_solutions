import sqlite3
from API_clases import *

connection = sqlite3.connect("API_COMPONENTS.db")
cursor = connection.cursor()

create_query = 'CREATE TABLE IF NOT EXISTS TODO (USER_ID INTEGER, ID INTEGER, TITLE TEXT, STATUS BOOLEAN)'
cursor.execute(create_query)

insert_query = 'INSERT INTO TODO VALUES (?,?,?,?)'
todo_objects = [Todos(d['userId'], d['id'], d['title'], d['completed']) for d in get_data("todos")]
for todo in todo_objects:
    cursor.execute(insert_query, todo.get_values())
#
# connection.commit()

#
# create_query = 'CREATE TABLE IF NOT EXISTS POSTS (USER_ID INTEGER, ID INTEGER, TITLE TEXT, BODY TEXT, COMMENTS )'
# cursor.execute(create_query)

