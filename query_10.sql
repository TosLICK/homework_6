-- Список курсів, які студенту з id=10 читає викладач з id=1
SELECT sub.id, sub.name
FROM subjects sub
JOIN grades g ON sub.id = g.subject_id
WHERE g.student_id = 10 AND sub.teacher_id = 1;