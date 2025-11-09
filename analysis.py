import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3

def load_data():
    conn = sqlite3.connect("student_data.db")
    df = pd.read_sql_query("SELECT * FROM students", conn)
    conn.close()
    return df

def show_analysis():
    df = load_data()
    print(df.describe())

    sns.pairplot(df[['assignment', 'midterm', 'attendance', 'final_score']])
    plt.show()

    plt.figure(figsize=(6, 4))
    df = df.dropna()
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Between Features")
    plt.show()

if __name__ == "__main__":
    show_analysis()
