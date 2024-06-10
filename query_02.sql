-- Знайти студента із найвищим середнім балом з предмета з id=2
SELECT s.id, s.fullname, ROUND(AVG(g.grade), 2) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.subject_id = 2
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 1;