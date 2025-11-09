# main.py
import tkinter as tk
from tkinter import ttk, messagebox
import database

database.connect_db()

def add_student():
    name = name_entry.get()
    roll = roll_entry.get()
    assignment = float(assignment_entry.get())
    midterm = float(midterm_entry.get())
    attendance = float(attendance_entry.get())

    database.insert_student(name, roll, assignment, midterm, attendance)
    messagebox.showinfo("Success", f"Student {name} added!")
    clear_fields()

def clear_fields():
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    assignment_entry.delete(0, tk.END)
    midterm_entry.delete(0, tk.END)
    attendance_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Student Grade Analyzer")
root.geometry("500x400")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Roll No").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Label(root, text="Assignment Marks").pack()
assignment_entry = tk.Entry(root)
assignment_entry.pack()

tk.Label(root, text="Midterm Marks").pack()
midterm_entry = tk.Entry(root)
midterm_entry.pack()

tk.Label(root, text="Attendance (%)").pack()
attendance_entry = tk.Entry(root)
attendance_entry.pack()

tk.Button(root, text="Add Student", command=add_student).pack(pady=10)

root.mainloop()
