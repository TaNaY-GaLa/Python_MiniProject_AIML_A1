import sqlite3

def connect_db():
    conn = sqlite3.connect("student_data.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        roll_no TEXT,
                        assignment REAL,
                        midterm REAL,
                        attendance REAL,
                        final_score REAL
                    )''')
    conn.commit()
    conn.close()

def insert_student(name, roll_no, assignment, midterm, attendance, final_score=None):
    conn = sqlite3.connect("student_data.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO students (name, roll_no, assignment, midterm, attendance, final_score)
                      VALUES (?, ?, ?, ?, ?, ?)''',
                   (name, roll_no, assignment, midterm, attendance, final_score))
    conn.commit()
    conn.close()

def fetch_all():
    conn = sqlite3.connect("student_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows
