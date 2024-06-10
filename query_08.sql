-- Знайти середній бал, який ставить викладач з id=1 зі своїх предметів
SELECT ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN subjects s ON g.subject_id = s.id
WHERE s.teacher_id = 1;