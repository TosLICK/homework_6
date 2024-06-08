DROP TABLE if exists groups;
CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

DROP TABLE if exists students;
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(150) NOT NULL,
    group_id INTEGER REFERENCES groups(id)
);

DROP TABLE if exists teachers;
CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(50) NOT NULL
);

DROP TABLE if exists subjects;
CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    teacher_id INTEGER REFERENCES teachers(id)
);

DROP TABLE if exists grades;
CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    grade INTEGER CHECK (grade >= 0 AND grade <= 100),
    grade_date DATE NOT NULL,
    student_id INTEGER REFERENCES students(id),
    subject_id INTEGER REFERENCES subjects(id)
);