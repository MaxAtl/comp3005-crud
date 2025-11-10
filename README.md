\# COMP3005 PostgreSQL CRUD (students)



\## What this is

A Python app that connects to PostgreSQL and performs CRUD on a `students` table



\## Requirements

\-PostgreSQL + pgAdmin installed locally

\-Python 3.9 or above



\## Database setup

1\. Create database `comp3005\_a3` in pgAdmin.

2\. Open Query Tool and run the script below to create the table and seed data:



==================================

CREATE TABLE IF NOT EXISTS students (

&nbsp; student\_id SERIAL PRIMARY KEY,

&nbsp; first\_name TEXT NOT NULL,

&nbsp; last\_name  TEXT NOT NULL,

&nbsp; email      TEXT NOT NULL UNIQUE,

&nbsp; enrollment\_date DATE

);



INSERT INTO students (first\_name, last\_name, email, enrollment\_date) VALUES

('John', 'Doe', 'john.doe@example.com', '2023-09-01'),

('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),

('Jim',  'Beam', 'jim.beam@example.com',  '2023-09-02')

ON CONFLICT DO NOTHING;

==================================





\#App setup for Windows. In terminal run:

==================================

python -m venv venv      

.\\venv\\Scripts\\Activate.ps1

pip install -r requirements.txt

==================================





\#Create a .env file with the following contents:

==================================

PGHOST=localhost

PGPORT=5432

PGDATABASE=comp3005\_a3

PGUSER=postgres

PGPASSWORD=REPLACE\_ME

==================================





\#Run the app:

==================================

python app.py  

==================================

