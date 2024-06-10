-- Знайти оцінки студентів у групі з id=1 з предмета з id=4
SELECT s.id, s.fullname, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.group_id = 1 AND g.subject_id = 4;