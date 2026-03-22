-- SQL Learning - Week 1-2
-- Basic queries from W3Schools

-- 1. Simple SELECT all columns
SELECT * FROM employees;

-- 2. SELECT specific columns
SELECT name, salary FROM employees;

-- 3. WHERE clause
SELECT * FROM employees WHERE department = 'IT';

-- 4. WHERE with comparison
SELECT * FROM employees WHERE salary > 50000;

-- 5. WHERE with AND/OR
SELECT * FROM employees 
WHERE (department = 'IT' OR department = 'Sales') 
AND salary > 45000;

-- 6. SELECT DISTINCT
SELECT DISTINCT department FROM employees;

-- 7. GROUP BY
SELECT department, COUNT(*) FROM employees GROUP BY department;
