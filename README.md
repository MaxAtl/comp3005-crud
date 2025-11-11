\#COMP3005 PostgreSQL CRUD (students)

Rashid Huseyn 101 298 637





\#Video Demo:

https://drive.google.com/file/d/12NTHg3KPEkhf1lol5vnGW4Tjy-eY7718/view?usp=sharing





\#What this is

A Python app that connects to PostgreSQL and performs CRUD on a `students` table:

-addStudent(...) – Create

-getAllStudents() – Read

\-updateStudentEmail(student\_id, new\_email) – Update

\-deleteStudent(student\_id) – Delete





\#Requirements

-PostgreSQL + pgAdmin installed locally

-Python 3.9 or above

-Packages: psycopg2-binary, python-dotenv (installed via requirements.txt)



\## Database setup

1\. Create database `comp3005\\\_a3` in pgAdmin.

2\. Open Query Tool and run the script below to create the table and seed data:

==================================

CREATE TABLE IF NOT EXISTS students (

  student\_id SERIAL PRIMARY KEY,

  first\_name TEXT NOT NULL,

  last\_name  TEXT NOT NULL,

  email      TEXT NOT NULL UNIQUE,

  enrollment\_date DATE

);



INSERT INTO students (first\_name, last\_name, email, enrollment\_date) VALUES

('John', 'Doe', 'john.doe@example.com', '2023-09-01'),

('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),

('Jim',  'Beam', 'jim.beam@example.com',  '2023-09-02')

ON CONFLICT DO NOTHING;



-- To Verify:

SELECT \* FROM students ORDER BY student\_id;

==================================

You should see three rows (John, Jane, Jim).





\#App setup for Windows



Project Files:

-app.py - application code (CRUD functions + CLI)

-requirements.txt - Python dependencies

-.env - database credentials (created by you; not committed)

-README.md - this file

&nbsp;

1)Create a .env file with the following contents:

==================================

PGHOST=localhost

PGPORT=5432

PGDATABASE=comp3005\_a3

PGUSER=postgres

PGPASSWORD=ReplacePassword

==================================

Make sure to replace the password with your PostgreSQL password. 


2)In windows terminal run:

==================================

python -m venv venv

.\\venv\\Scripts\\Activate.ps1

python -m pip install --upgrade pip

pip install -r requirements.txt

==================================



3)Run the app:

==================================

python app.py list

python app.py add "Alice" "Wonder" "alice.wonder@example.com" 2023-09-03

python app.py update <ID> "alice.w@example.com"

python app.py delete <ID>

==================================



4)After each operation, you can verify in pgAdmin Query Tool by running:

==================================

SELECT \* FROM students ORDER BY student\_id;

==================================

