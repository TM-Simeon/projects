from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker
from createdb import users_table, engine, students

# create a database engine
# engine = create_engine('sqlite:///mydatabase.db', echo=True)

# create a session factory
Session = sessionmaker(bind=engine)

metadata = MetaData()

# create a session object
session = Session()

# search for a user by name
name_to_search = 'John Doe1'
result = session.query(users_table).filter_by(name=name_to_search).first()

if result is not None:
    print(f"User found with id {result['id']}")
else:
    print(f"No user found with name {name_to_search}")

result2 = session.query(students).filter_by(name=name_to_search).first()

if result is not None:
    # print(result2)
    print(f"User found with phone number: {result2['phone_number']}")
else:
    print(f"No user found with name {name_to_search}")
# close the session
session.close()





