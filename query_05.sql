-- Знайти які курси читає викладач з id=4
SELECT s.id, s.name
FROM subjects s
WHERE s.teacher_id = 4;