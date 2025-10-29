import streamlit as st
import pickle, os, sys

# Add parent path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.preprocess_utils import clean_tweet_text
from utils.db_connection import log_prediction

# --- Load Model and Vectorizer ---
model_path = os.path.join(os.path.dirname(__file__), "../models/sentiment_model.pkl")
with open(model_path, "rb") as f:
    model, tfidf = pickle.load(f)

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="Citizen Complaint Analyzer",
    page_icon="💬",
    layout="centered",
)

# --- Custom CSS for Styling ---
st.markdown(
    """
    <style>
    /* Overall page style */
    .main {
        background-color: #0e1117;
        color: #ffffff;
        font-family: 'Poppins', sans-serif;
    }

    /* Header style */
    .title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 10px;
        background: linear-gradient(90deg, #00b4d8, #0077b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitle {
        text-align: center;
        color: #cfd3dc;
        font-size: 1rem;
        margin-bottom: 30px;
    }

    /* Text area */
    textarea {
        background-color: #1e1e1e !important;
        color: #ffffff !important;
        border-radius: 10px !important;
        border: 1px solid #00b4d8 !important;
    }

    /* Buttons */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #00b4d8, #0077b6);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 25px;
        font-size: 16px;
        font-weight: 500;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background: linear-gradient(90deg, #0077b6, #00b4d8);
        transform: scale(1.05);
    }

    /* Result boxes */
    .result-box {
        padding: 15px;
        border-radius: 10px;
        font-weight: 600;
        text-align: center;
        font-size: 1.1rem;
        margin-top: 20px;
    }

    .complaint {
        background-color: #ffcccc;
        color: #660000;
    }

    .non-complaint {
        background-color: #2e7d32;
        color: #ffffff;
    }

    /* Info box style */
    .log-info {
        background-color: #1f2a44;
        padding: 10px;
        border-radius: 8px;
        color: #cfd3dc;
        font-size: 0.9rem;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- App Header ---
st.markdown("<h1 class='title'>💬 Citizen Complaint & Grievance Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Enter a tweet or complaint text below to check if it expresses a <b>citizen grievance</b> or not.</p>", unsafe_allow_html=True)

# --- User Input Section ---
user_input = st.text_area("✍️ Enter tweet text:", height=150)

# --- Analyze Button ---
if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text first.")
    else:
        # Preprocess and Predict
        clean_text = clean_tweet_text(user_input)
        vectorized = tfidf.transform([clean_text])
        prediction = model.predict(vectorized)[0]

        # --- Assign label and style ---
        if prediction == 1:
            label_text = "Complaint / Grievance 🚨"
            box_class = "complaint"
        else:
            label_text = "Non-Complaint ✅"
            box_class = "non-complaint"

        # --- Display Result Section ---
        st.markdown("<h3>Result:</h3>", unsafe_allow_html=True)
        st.markdown(f"<div class='result-box {box_class}'>Predicted Label: {label_text}</div>", unsafe_allow_html=True)
        st.markdown(f"<br><b>Cleaned text used for analysis:</b> {clean_text}", unsafe_allow_html=True)

        # --- Log to Database ---
        try:
            log_prediction(user_input, clean_text, label_text)
            st.markdown("<div class='log-info'>📦 Result logged successfully to database.</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"❌ Could not log to database: {e}")

# --- Footer ---
st.markdown("<br><hr><center>© 2025 Citizen Grievance Mini Project | Built with ❤️ using Streamlit</center>", unsafe_allow_html=True)
