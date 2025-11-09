import tkinter as tk
from tkinter import ttk, messagebox
from model import predict_score

def predict():
    try:
        a = float(entry_assignment.get())
        m = float(entry_midterm.get())
        att = float(entry_attendance.get())
        pred = predict_score(a, m, att)
        pred = max(0, min(100, pred))
        result_label.config(
            text=f"🎯 Predicted Final Score: {pred}%",
            foreground="#0A6847",
            font=("Segoe UI", 12, "bold")
        )
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for all fields.")

root = tk.Tk()
root.title("📘 Student Final Score Predictor")
root.geometry("420x400")
root.resizable(False, False)
root.configure(bg="#E9F5DB")

# Title Frame
title = tk.Label(
    root, text="Student Grade Predictor",
    font=("Segoe UI", 16, "bold"), bg="#E9F5DB", fg="#134B70"
)
title.pack(pady=20)

# Input Frame
frame = ttk.Frame(root, padding=20)
frame.pack()

style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("TEntry", padding=5)

ttk.Label(frame, text="Assignment Marks (0-100):").grid(row=0, column=0, sticky="w", pady=5)
entry_assignment = ttk.Entry(frame, width=20)
entry_assignment.grid(row=0, column=1, pady=5)

ttk.Label(frame, text="Midterm Marks (0-100):").grid(row=1, column=0, sticky="w", pady=5)
entry_midterm = ttk.Entry(frame, width=20)
entry_midterm.grid(row=1, column=1, pady=5)

ttk.Label(frame, text="Attendance (%):").grid(row=2, column=0, sticky="w", pady=5)
entry_attendance = ttk.Entry(frame, width=20)
entry_attendance.grid(row=2, column=1, pady=5)

# Predict Button
predict_btn = tk.Button(
    root, text="Predict Final Score", command=predict,
    bg="#134B70", fg="white", font=("Segoe UI", 11, "bold"),
    relief="flat", padx=20, pady=10, cursor="hand2", activebackground="#0F3057"
)
predict_btn.pack(pady=20)

# Result Label
result_label = tk.Label(
    root, text="", bg="#E9F5DB", font=("Segoe UI", 12)
)
result_label.pack(pady=10)


root.eval('tk::PlaceWindow . center')
root.mainloop()
