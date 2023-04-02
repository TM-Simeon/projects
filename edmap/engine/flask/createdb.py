from sqlalchemy import Table, MetaData
from sqlalchemy.engine.reflection import Inspector
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
# from sqlalchemy.orm import relationship, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# create a database engine
engine = create_engine('sqlite:///db.db', echo=False)

metadata = MetaData()

# define the users table
users = Table('users', metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String),
                Column('age', Integer),
                Column('email', String),
)
# define the students table

students = Table('students', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('user_id', Integer, ForeignKey('users.id')),
                 Column('name', String),
                 Column('email', String),
                 Column('password', String),
                 Column('date_of_birth', Date),
                 Column('gender', String),
                 Column('address', String),
                 Column('phone_number', String)
                 )

courses = Table('courses', metadata,
                Column('id', Integer, primary_key=True),
                Column('title', String),
                Column('description', String),
                Column('instructor_id', Integer, ForeignKey('instructors.id')),
                Column('grade_level', Integer),
                Column('start_date', Date),
                Column('end_date', Date)
                )

instructors = Table('instructors', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String),
                    Column('email', String),
                    Column('password', String),
                    Column('date_of_birth', Date),
                    Column('gender', String),
                    Column('address', String),
                    Column('phone_number', String)
                    )

enrollments = Table('enrollments', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('student_id', Integer, ForeignKey('students.id')),
                    Column('course_id', Integer, ForeignKey('courses.id')),
                    Column('enrollment_date', Date),
                    Column('completion_date', Date),
                    Column('grade', Integer)
                    )

# create the database if it doesn't exist
inspector = Inspector.from_engine(engine)
if not inspector.has_table('users'):
    metadata.create_all(engine)
    print("Database created successfully.")
else:
    # print("Database already exists.")
    pass

# create the tables if they don't exist
if not inspector.has_table('students'):
    metadata.create_all(engine)
    print("students table created successfully.")
else:
    # print("students table already exist.")
    pass
    

if not inspector.has_table('courses'):
    metadata.create_all(engine)
    print("courses table created successfully.")
else:
    # print("course table already exist.")
    pass
    
if not inspector.has_table('instructors'):
    metadata.create_all(engine)
    print("instructors table created successfully.")
else:
    # print("isntructors table already exist.")
    pass
    

if not inspector.has_table('enrollments'):
    metadata.create_all(engine)
    print("enrollment table created successfully.")
else:
    # print("enrollment table already exist.")
    pass