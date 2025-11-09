import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import sqlite3, os, joblib

def train_model():
    os.makedirs("models", exist_ok=True)
    conn = sqlite3.connect("student_data.db")
    df = pd.read_sql_query("SELECT * FROM students WHERE final_score IS NOT NULL", conn)
    conn.close()

    X = df[['assignment', 'midterm', 'attendance']]
    y = df['final_score']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    joblib.dump(model, "models/final_score_model.pkl")
    print("✅ Model trained and saved!")

    preds = model.predict(X_test)
    print(f"R2 Score: {r2_score(y_test, preds):.2f}")

def predict_score(assignment, midterm, attendance):
    model = joblib.load("models/final_score_model.pkl")
    pred = model.predict([[assignment, midterm, attendance]])
    return round(pred[0], 2)

if __name__ == "__main__":
    train_model()
    print("Example prediction:")
    test_pred = predict_score(100, 100, 100)
    test_pred = max(0, min(100, test_pred))
    print(f"Predicted Final Score for perfect student: {test_pred}")
