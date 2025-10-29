# 💬 Citizen Complaint & Grievance Analyzer

### *Mini Project based on Twitter Complaint Classification & Sentiment Analysis*

---

## 🧭 Overview
This mini-project is inspired by research on *citizen-centric complaint and grievance redressal systems*.
It automatically analyzes citizen tweets or text inputs to determine whether they represent a **complaint/grievance** or a **non-complaint**, using **machine learning** and **NLP** techniques.

The system connects with a **MySQL database**, performs **text preprocessing**, **model inference**, and presents the results on an interactive **Streamlit dashboard**.

---

## 🏗️ Project Architecture

```
citizen_grievance_project/
│
├── data/
│   ├── Complaints_Reports_Data.sql
│   ├── tweets_sample.csv
│   ├── cleaned_annotated.csv
│
├── notebooks/
│   ├── data_preprocessing.ipynb
│   ├── sentiment_model_training.ipynb
│
├── models/
│   ├── sentiment_model.pkl
│
├── app/
│   ├── dashboard_app.py
│
├── utils/
│   ├── db_connection.py
│   ├── preprocess_utils.py
│
└── README.md
```

---

## ⚙️ System Requirements

- **Processor:** 64-bit (x64)
- **Python:** 3.11+
- **Database:** MySQL 8.x
- **Tools:** VS Code, Google Colab

---

## 📦 Dependencies

Install dependencies:
```bash
pip install streamlit mysql-connector-python scikit-learn pandas numpy
```

For Colab training:
```bash
!pip install scikit-learn pandas numpy
```

---

## 🧩 Development Steps

### STEP 1 — Data Setup
- Import `Complaints_Reports_Data.sql` into MySQL.
- Verify tables: `annotated`, `posts`, `users`, etc.
- Create sample dataset `tweets_sample.csv` (150 tweets).

### STEP 2 — Folder Setup
Organize the project as shown above.

### STEP 3 — Data Preprocessing
- Use `db_connection.py` to connect to MySQL.
- Clean tweets using `preprocess_utils.py`.
- Save results to `cleaned_annotated.csv`.

### STEP 4 — Model Training
- Use TF-IDF + Logistic Regression in Colab.
- Accuracy achieved: **75%** (baseline).

```
precision    recall  f1-score   support
0 (Non-Complaint)  0.74  0.84  0.79  409
1 (Complaint)      0.76  0.63  0.69  331
accuracy                             0.75
```

### STEP 5 — Streamlit Dashboard
- Input tweet → Clean → Predict → Log result to MySQL.
- Displays predicted label and cleaned text.

---

## 🧠 Dashboard Features

✅ Modern responsive UI  
✅ Light red box for complaints, green for non-complaints  
✅ Logs all predictions to MySQL  
✅ Displays cleaned text & success message  

---

## 🖼️ Example Output

**Input:**  
> The staff in the hospital was rude and didn't attend properly. 

**Output:**  
```
Predicted Label: Complaint / Grievance 🚨
Cleaned text used for analysis: the staff in the hospital was rude and didnt attend properly
📦 Result logged successfully to database.
```

**Input:**  
> This online grievance system is good and easy to use. 

**Output:**  
```
Predicted Label: Non-Complaint ✅
Cleaned text used for analysis: this online grievance system is good and easy to use
📦 Result logged successfully to database.
```

---

## 🧰 Database Reset Query

To clean the table for a fresh start:
```sql
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE analysis_logs;
SET FOREIGN_KEY_CHECKS = 1;
```

---

## 🚀 Run the App

```bash
streamlit run app/dashboard_app.py
```

Then open:
```
http://localhost:8501
```

---

## 📊 Future Enhancements

1. Improve model accuracy (more data, class balancing)
2. Upgrade to BERT/DistilBERT
3. Add admin dashboard analytics
4. Integrate REST API for web/mobile apps

---

## 📚 References

- Research: *“Entity Based Sentiment Analysis on Twitter - Siddharth Batra and Deepak Rao (Stanford University)”*
- [Scikit-learn Docs](https://scikit-learn.org)
- [Streamlit Docs](https://streamlit.io)

---

## ⚙️ Tools Used

Python, Streamlit, MySQL, Google Colab

---

## 🏁 Summary

An end-to-end **citizen grievance detection pipeline**:
**Data → Preprocessing → Model Training → Web Dashboard → Database Logging**.

Built as a fully functional **mini-project** for real-time complaint classification and public governance analytics.

---
