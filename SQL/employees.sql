CREATE TABLE employees(
	emp_no INT PRIMARY KEY,
	birth_date DATE NOT NULL,
	first_name VARCHAR NOT NULL,
	last_name VARCHAR NOT NULl,
	gender char(1) NOT NULL,
	hire_date DATE NOT NULL
)
CREATE TABLE departments(
	dept_no VARCHAR PRIMARY KEY,
	dept_name VARCHAR UNIQUE NOT NULL
)
CREATE TABLE titles(
	emp_no INT REFERENCES employees(emp_no),
	title VARCHAR NOT NULL,
	from_date DATE NOT NULL,
	to_date DATE NOT NULL,
	PRIMARY KEY (emp_no, from_date)
)
CREATE TABLE salary(
	emp_no INT PRIMARY KEY REFERENCES employees(emp_no),
	salary NUMERIC,
	from_date DATE NOT NULL,
	to_date DATE
)
CREATE TABLE dept_manager(
	dept_no VARCHAR REFERENCES departments(dept_no),
	emp_no INT REFERENCES employees(emp_no),
	from_date DATE NOT NULL,
	to_date DATE,
	PRIMARY KEY (dept_no, emp_no)
)
CREATE TABLE dept_emp(
	emp_no INT REFERENCES employees(emp_no),
	dept_no VARCHAR REFERENCES departments(dept_no),
	from_date DATE NOT NULL,
	to_date DATE, 
	PRIMARY KEY(emp_no, dept_no)
);