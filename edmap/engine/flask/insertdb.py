from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Table, MetaData
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.engine.reflection import Inspector
from createdb import engine, students, users
from datetime import datetime


# Create the engine
# engine = create_engine('sqlite:///db.db')

# Create the metadata
# metadata = MetaData()
Session = sessionmaker(bind=engine)
session = Session()

# Insert data into the users table
def insertUser(data):
    user_data = {
        'name': data['name'],
        'age': data['age'],
        'email': data['email']
    }
    ins = users.insert().values(**user_data)
    session.execute(ins)
    session.commit()
    session.close()

# Insert data into the students table
def insertStudent(data):
    student_data = {
        'name': 'John Doe',
        'email': 'johndoe@example.com',
        'password': 'password123',
        'date_of_birth': datetime.now(),
        'gender': 'Male',
        'address': '123 Main Street',
        'phone_number': '555-1234'
    }
    ins = students.insert().values(**student_data)
    session.execute(ins)
    session.commit()
    session.close()

# close the session
# session.close()

