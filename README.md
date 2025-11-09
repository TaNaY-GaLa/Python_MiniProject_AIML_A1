# Python_MiniProject_AIML_A1

# Student Performance Intelligence Suite

A clean, modular, and scalable Python application designed to **store student data**, **analyze academic performance**, and **predict final scores** using lightweight machine learning models. The project blends Tkinter-based GUIs, SQLite-backed persistence, and scikit-learn models to deliver a complete academic analytics toolkit.

---

## Key Features

### Academic Data Hub
- Add and maintain student records through an intuitive Tkinter interface.
- Record assignment scores, midterm performance, attendance, and optional final scores.
- Data is securely stored in a local SQLite database.

### Predictive Analytics
- Linear Regression model trained on real or synthetic student data.
- Predicts final scores based on assignment marks, midterm marks, and attendance.
- Clean GUI to input parameters and instantly view predictions.

### Data Insights & Visualization
- Summary statistics (mean, SD, percentiles) via Pandas.
- Correlation analysis and visual heatmaps.
- Pairwise relationships plotted using Seaborn.

### Automated Dataset Generation
- Synthetic student records generated for testing and prototyping.
- Ideal for demos, academic submissions, and early-stage ML experimentation.

---

## Project Structure

```
.
├── main.py            # GUI for adding new student records
├── gui.py             # GUI for ML-based final score prediction
├── model.py           # Training pipeline and prediction utilities
├── analysis.py        # Data exploration and visual reports
├── database.py        # SQLite operations and schema management
├── generate_data.py   # Synthetic dataset generator
├── student_data.db    # SQLite database (auto-created)
└── models/            # Saved ML artifacts (auto-created)
```

---

## Installation & Setup

### 1. Environment
Use Python 3.9 or above.

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate        # Windows
```

### 2. Install dependencies
```bash
pip install pandas matplotlib seaborn scikit-learn joblib
```

### 3. Initialize or Populate Database
Populate sample records using:
```bash
python generate_data.py
```
Or enter records manually using:
```bash
python main.py
```

### 4. Train the Prediction Model
```bash
python model.py
```
This generates `models/final_score_model.pkl`.

### 5. Launch the Prediction GUI
```bash
python gui.py
```

### 6. Run Exploratory Data Analysis
```bash
python analysis.py
```

---

## Technical Design

### Storage Layer
- SQLite database (`student_data.db`)
- Auto-created table: `students`  
  Contains: name, roll_no, assignment, midterm, attendance, final_score.

### ML Pipeline
- Linear Regression (lightweight & interpretable)
- 80/20 train–test split
- Model persisted using joblib
- Scaled for small to medium datasets

### GUI System
- Tkinter-based dual-window architecture
- Input validation and error handling
- Prediction UI auto-limits score between 0 and 100 for realism

---

## Future Enhancements

- Switch to Ridge/Lasso for more stable predictions on noisy data.
- Improve GUI design with ttk themes and progress indicators.
- Add analytics dashboard (aggregate charts, trends, and ranking).
- Export reports to PDF or Excel.
- Integrate Flask or FastAPI to convert into a web-based system.

---

## License
You may add MIT, Apache-2.0, or another license based on distribution needs.

