import os
from datetime import date
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv()  # reads .env

def get_connection():
    """
    Opens and returns a new DB connection using environment variables.
    """
    return psycopg2.connect(
        host=os.getenv("PGHOST", "localhost"),
        port=os.getenv("PGPORT", "5432"),
        dbname=os.getenv("PGDATABASE", "comp3005_a3"),
        user=os.getenv("PGUSER", "postgres"),
        password=os.getenv("PGPASSWORD", ""),
        cursor_factory=RealDictCursor
    )

def getAllStudents():
    """
    Retrieves and prints all student records.
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT student_id, first_name, last_name, email, enrollment_date FROM students ORDER BY student_id;")
            rows = cur.fetchall()
            print("\n== All Students ==")
            for r in rows:
                print(f"{r['student_id']}: {r['first_name']} {r['last_name']} | {r['email']} | enrolled {r['enrollment_date']}")
    # connection auto-committed on close when no writes are pending

def addStudent(first_name, last_name, email, enrollment_date):
    """
    Inserts a new student row. Returns the new student_id.
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO students (first_name, last_name, email, enrollment_date)
                VALUES (%s, %s, %s, %s)
                RETURNING student_id;
            """, (first_name, last_name, email, enrollment_date))
            new_id = cur.fetchone()["student_id"]
            conn.commit()
            print(f"\n== Added student_id {new_id}: {first_name} {last_name} ({email}) ==")
            return new_id

def updateStudentEmail(student_id, new_email):
    """
    Updates the email for the given student_id.
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE students
                SET email = %s
                WHERE student_id = %s;
            """, (new_email, student_id))
            if cur.rowcount == 0:
                print(f"\n!! No student found with id {student_id}")
            else:
                conn.commit()
                print(f"\n== Updated student_id {student_id} email to {new_email} ==")

def deleteStudent(student_id):
    """
    Deletes the row with the given student_id.
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
            if cur.rowcount == 0:
                print(f"\n!! No student found with id {student_id}")
            else:
                conn.commit()
                print(f"\n== Deleted student_id {student_id} ==")

if __name__ == "__main__":
    # 1) Show initial data
    getAllStudents()

    # 2) Create a new student
    new_id = addStudent("Alice", "Wonder", "alice.wonder@example.com", date(2023, 9, 3))

    # 3) Verify insert
    getAllStudents()

    # 4) Update that student's email
    updateStudentEmail(new_id, "alice.w@example.com")

    # 5) Verify update
    getAllStudents()

    # 6) Delete that student
    deleteStudent(new_id)

    # 7) Final verify
    getAllStudents()