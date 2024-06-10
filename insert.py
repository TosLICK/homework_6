from random import randint
from faker import Faker
from connect import create_connection

fake = Faker('uk_UA')


def seed_groups(number_groups=3):
    groups = [fake.word() for _ in range(number_groups)]
    sql = "INSERT INTO groups (name) VALUES (%s);"
    with create_connection() as conn:
        with conn.cursor() as cur:
            cur.executemany(sql, [(group,) for group in groups])
        conn.commit()

def seed_students(number_students=40):
    students = [(fake.name(), randint(1, 3)) for _ in range(number_students)]
    sql = "INSERT INTO students (fullname, group_id) VALUES (%s, %s);"
    with create_connection() as conn:
        with conn.cursor() as cur:
            cur.executemany(sql, students)
        conn.commit()

def seed_teachers(number_teachers=5):
    teachers = [fake.name() for _ in range(number_teachers)]
    sql = "INSERT INTO teachers (fullname) VALUES (%s);"
    with create_connection() as conn:
        with conn.cursor() as cur:
            cur.executemany(sql, [(teacher,) for teacher in teachers])
        conn.commit()

def seed_subjects(number_subjects=7):
    subjects = [(fake.word(), randint(1, 5)) for _ in range(number_subjects)]
    sql = "INSERT INTO subjects (name, teacher_id) VALUES (%s, %s);"
    with create_connection() as conn:
        with conn.cursor() as cur:
            cur.executemany(sql, subjects)
        conn.commit()

def seed_grades(number_subjects=7):
    subjects = [(fake.word(), randint(1, 5)) for _ in range(number_subjects)]
    sql = "INSERT INTO subjects (name, teacher_id) VALUES (%s, %s);"
    with create_connection() as conn:
        with conn.cursor() as cur:
            cur.executemany(sql, subjects)
        conn.commit()

def seed_grades():
    sql = "INSERT INTO grades (grade, grade_date, student_id, subject_id) VALUES (%s, %s, %s, %s)"
    grades = []
    for student_id in range(1, 41):
        subject_id = 1
        for _ in range(randint(7, 20)):
            grade = (randint(0, 100), fake.date_this_decade(), student_id, subject_id)
            grades.append(grade)
            if subject_id == 7:
                subject_id = 1
                continue
            subject_id += 1
    with create_connection() as conn:
        with conn.cursor() as cur:
            cur.executemany(sql, grades)
        conn.commit()


if __name__ == "__main__":
    seed_teachers()
    seed_groups()
    seed_students()
    seed_subjects()
    seed_grades()
