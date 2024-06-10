DROP TABLE IF EXISTS groups cascade;
CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

DROP TABLE IF EXISTS students cascade;
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(150) NOT NULL,
    group_id INTEGER REFERENCES groups(id)
        ON DELETE CASCADE
);

DROP TABLE IF EXISTS teachers cascade;
CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(50) NOT NULL
);

DROP TABLE IF EXISTS subjects cascade;
CREATE TABLE subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    teacher_id INTEGER REFERENCES teachers(id)
        ON DELETE CASCADE
);

DROP TABLE IF EXISTS grades cascade;
CREATE TABLE grades (
    id SERIAL PRIMARY KEY,
    grade INTEGER CHECK (grade >= 0 AND grade <= 100),
    grade_date DATE NOT NULL,
    student_id INTEGER REFERENCES students(id)
        ON DELETE CASCADE,
    subject_id INTEGER REFERENCES subjects(id)
        ON DELETE CASCADE
);