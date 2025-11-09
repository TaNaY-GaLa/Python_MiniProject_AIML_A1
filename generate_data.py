import random
import database

database.connect_db()

for i in range(1, 101):
    name = f"Student{i}"
    roll_no = str(i)
    assignment = random.randint(40, 100)
    midterm = random.randint(35, 100)
    attendance = random.randint(60, 100)
    final_score = int(assignment*0.3 + midterm*0.4 + attendance*0.3 + random.randint(-5,5))
    database.insert_student(name, roll_no, assignment, midterm, attendance, final_score)

print("✅ 100 synthetic student records added!")
