import mysql.connector
from datetime import datetime

def get_connection():
    """
    Connect to MySQL database 'citizen_complaints_sampled'
    """
    connection = mysql.connector.connect(
        host="localhost",
        user="root",               # your MySQL username
        password="BM@210504MAY",  # your MySQL password
        database="citizen_complaints_sampled"
    )
    return connection

def log_prediction(raw_text, cleaned_text, label):
    """
    Store each analyzed tweet/complaint into the database.
    """
    conn = get_connection()
    cursor = conn.cursor()
    query = """
        INSERT INTO analysis_logs (raw_text, cleaned_text, predicted_label, created_at)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (raw_text, cleaned_text, label, datetime.now()))
    conn.commit()
    cursor.close()
    conn.close()


def fetch_sample_data():
    """
    Fetch some records from 'posts' or 'annotated' table to verify connection.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    print("✅ Tables in Database:", cursor.fetchall())

    # Example: fetch a few posts
    cursor.execute("SELECT * FROM posts LIMIT 5;")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    fetch_sample_data()
