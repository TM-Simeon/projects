import sqlite3
import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()
query = 'insert into users(name, age, email) values("simeon",36,"simeon@gmail.com");'
cursor.execute(query)
conn.commit()
conn.close()