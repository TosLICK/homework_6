-- Знайти середній бал у групах з предмета з id=4
SELECT gr.id, gr.name, ROUND(AVG(g.grade), 2) AS average_grade
FROM groups gr
JOIN students s ON gr.id = s.group_id
JOIN grades g ON s.id = g.student_id
WHERE g.subject_id = 4
GROUP BY gr.id;