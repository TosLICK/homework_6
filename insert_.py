import logging
from random import randint
from faker import Faker
from psycopg2 import DatabaseError

# from connect import create_connection


fake = Faker('uk-Ua')

def insert_data_groups(conn):
    c = conn.cursor()
    try:
        for _ in range(3):
            c.execute('INSERT INTO groups (name) VALUES (%s)', (fake.word(),))
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()

def insert_data_students(conn):
    c = conn.cursor()
    try:
        for _ in range(randint(30, 50)):
            c.execute('INSERT INTO students (fullname, group_id) VALUES (%s, %s)',
                     (fake.name(), randint(1, 3)))
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()

def insert_data_teachers(conn):
    c = conn.cursor()
    try:
        for _ in range(randint(3, 5)):
            c.execute('INSERT INTO teachers (fullname) VALUES (%s)', (fake.name(),))
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()

def insert_data_subjects(conn):
    c = conn.cursor()
    c.execute('SELECT MAX(id) from "teachers"')
    teachers = int(c.fetchone()[0])
    try:
        for _ in range(randint(5, 8)):
            c.execute('INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)',
                     (fake.word(), randint(1, teachers)))
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()

def insert_data_grades(conn):
    c = conn.cursor()
    c.execute('SELECT MAX(id) from "students"')
    students = int(c.fetchone()[0])
    c.execute('SELECT MAX(id) from "subjects"')
    subjects = int(c.fetchone()[0])
    try:
        for student_id in range(1, students + 1):
            subject_id = 1
            for _ in range(randint(subjects, 20)):
                c.execute('INSERT INTO grades (grade, grade_date, student_id, subject_id) VALUES (%s, %s, %s, %s)',
                         (randint(0, 100), fake.date_this_decade(), student_id, subject_id))
                if subject_id == subjects:
                    subject_id = 1
                    continue
                subject_id += 1
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()
