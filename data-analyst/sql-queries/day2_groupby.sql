-- 1. Count employees per department
SELECT department, COUNT(*) as count FROM employees GROUP BY department;

-- 2. Sum salaries per department
SELECT department, SUM(salary) as total_salary FROM employees GROUP BY department;

-- 3. Average salary per department
SELECT department, AVG(salary) as avg_salary FROM employees GROUP BY department;

-- 4. GROUP BY with HAVING (departments with avg salary > 48000)
SELECT department, AVG(salary) as avg_salary FROM employees GROUP BY department HAVING AVG(salary) > 48000;

-- 5. Count and sum together
SELECT department, COUNT(*) as emp_count, SUM(salary) as total FROM employees GROUP BY department;
