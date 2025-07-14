-- SQL Practice from Leetcode

-- 2356
SELECT teacher_id, COUNT(DISTINCT subject_id) cnt
FROM Teacher
GROUP BY teacher_id
;

-- 1757
SELECT product_id
FROM Products
WHERE low_fats = 'Y'
AND recyclable = 'Y'
;

-- 1741
WITH times AS
(
    SELECT event_day as `day`, emp_id, (out_time - in_time) as total_time
    FROM Employees
)
SELECT `day`, emp_id, SUM(total_time) as total_time
FROM times
GROUP BY `day`, emp_id
;

