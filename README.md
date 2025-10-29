📘 Citizen Complaint & Grievance Analyzer
Mini Project based on Twitter Complaint Classification & Sentiment Analysis
🧭 Overview

This mini-project is inspired by the research work on citizen-centric complaint and grievance redressal systems.
It automatically analyzes citizen tweets or text inputs to determine whether they represent a complaint/grievance or a non-complaint, using machine learning and NLP techniques.

The system connects with a MySQL database, performs text preprocessing, model inference, and presents the results on an interactive Streamlit dashboard.

🏗️ Project Architecture
grievance_analysis_project/
│
├── data/
│   ├── Complaints_Reports_Data.sql         # Original SQL dump (tables: posts, annotated, etc.)
│   ├── tweets_sample.csv                   # Small sample dataset (150 tweets for demo)
│   ├── cleaned_annotated.csv               # Cleaned dataset after preprocessing
│
├── notebooks/
│   ├── data_preprocessing.ipynb            # Notebook for preprocessing and loading from SQL
│   ├── sentiment_model_training.ipynb      # Model training (TF-IDF + Logistic Regression)
│
├── models/
│   ├── sentiment_model.pkl                 # Trained ML model + TF-IDF vectorizer (pickle)
│
├── app/
│   ├── dashboard_app.py                    # Streamlit-based web dashboard
│
├── utils/
│   ├── db_connection.py                    # Database connection & logging functions
│   ├── preprocess_utils.py                 # Text cleaning, loading, and transformation utilities
│
└── README.md

⚙️ System Requirements

Processor: 64-bit (x64)

Python: 3.11 or above

Database: MySQL 8.x

Development Tools: VS Code (for app) + Google Colab (for model training)

📦 Dependencies

Install all required packages using:

pip install streamlit mysql-connector-python scikit-learn pandas numpy


If training in Colab:

!pip install scikit-learn pandas numpy

🧩 Step-by-Step Development Process
STEP 1 — Data Setup

Imported SQL dataset Complaints_Reports_Data.sql into MySQL Workbench.

Verified tables: annotated, posts, users, hashtags, etc.

Created a small CSV (tweets_sample.csv) with 150 synthetic tweets for testing.

STEP 2 — Folder & File Structure

Organized all project modules in VS Code according to standard modular architecture (see above).

STEP 3 — Data Preprocessing

Connected to MySQL using utils/db_connection.py.

Cleaned and normalized tweets (preprocess_utils.py) by removing URLs, mentions, hashtags, and special characters.

Exported the processed text to cleaned_annotated.csv.

Saved cleaned sample output for inspection.

STEP 4 — Model Training (Google Colab)

Loaded cleaned dataset.

Used TF-IDF Vectorizer to convert text → numerical features.

Trained Logistic Regression classifier.

Achieved 75% accuracy (baseline performance).

Exported (model, vectorizer) as sentiment_model.pkl.

Example performance:

precision    recall  f1-score   support
0 (Non-Complaint)  0.74      0.84      0.79       409
1 (Complaint)      0.76      0.63      0.69       331
accuracy                               0.75

STEP 5 — Streamlit Dashboard Development

Developed an interactive web app (app/dashboard_app.py) that:

Takes user input (tweet or complaint text).

Cleans it using preprocess_utils.

Vectorizes and classifies using the saved model.

Logs the result to the database.

Displays the predicted label and cleaned text in a styled UI.

🧠 Dashboard Features

✅ Clean modern interface (dark-theme adaptive).
✅ Predicts “Complaint” or “Non-Complaint” instantly.
✅ Logs each prediction to MySQL for analytics.
✅ Light red color for Complaints and green for Non-Complaints.
✅ Displays cleaned text and confirmation of DB logging.

🖼️ Example Output

Input:

The staff in the hospital was rude and didn't attend properly.

Output:

Predicted Label: Complaint / Grievance 🚨
Cleaned text used for analysis: the staff in the hospital was rude and didnt attend properly
📦 Result logged successfully to database.

🧰 Database Commands

To clear the previous logs and start fresh:

SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE predictions;
SET FOREIGN_KEY_CHECKS = 1;


(Replace predictions with your actual logging table name if different.)

🚀 Running the App

In your terminal (inside project root):

streamlit run app/dashboard_app.py


You’ll see:

Local URL: http://localhost:8501
Network URL: http://<your-ip>:8501


Open the Local URL in your browser to access the dashboard.

📊 Future Enhancements

Improve Model Accuracy

Add more labeled data.

Balance class weights or use class_weight='balanced'.

Use n-grams (1–3) for better context capture.

Advanced Models

Upgrade to BERT or DistilBERT for semantic understanding.

Incorporate emotion/sentiment scores.

Admin Dashboard

Add a Streamlit sidebar for live analytics:

Complaint frequency.

Department tagging (Water, Power, Road, etc.).

API Integration

Create Flask/REST API for use in mobile or web portals.

📚 References

“Entity Based Sentiment Analysis on Twitter - by Sidhartha Batra and Deepak Rao(Stanford University)” (Research Paper)

Scikit-learn Documentation: https://scikit-learn.org

Streamlit Documentation: https://streamlit.io


⚙️ Tools Used
Python, Streamlit, MySQL, Google Colab
—	—	—

🏁 Summary

This mini project demonstrates an end-to-end citizen grievance detection pipeline:
Data → Preprocessing → Model Training → Web Dashboard → Database Logging.

It serves as a working prototype for integrating AI-based complaint classification into e-governance platforms or social media analytics systems.