-- Знайти список студентів у групі з id=1
SELECT s.id, s.fullname
FROM students s
WHERE s.group_id = 1
order by s.fullname;