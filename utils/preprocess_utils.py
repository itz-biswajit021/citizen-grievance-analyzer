import re
import string
import pandas as pd

def clean_tweet_text(text):
    """
    Clean tweet text: remove mentions, URLs, hashtags, punctuation, and extra spaces.
    """
    text = re.sub(r"http\S+", "", text)             # remove URLs
    text = re.sub(r"@\w+", "", text)                # remove mentions
    text = re.sub(r"#\w+", "", text)                # remove hashtags
    text = re.sub(r"&amp;", "and", text)            # decode ampersand
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)  # remove punctuation
    text = re.sub(r"\s+", " ", text).strip()        # normalize spaces
    return text.lower()

def load_and_clean_from_db(connection):
    """
    Fetch annotated data and clean text for sentiment/classification training.
    """
    query = "SELECT * FROM annotated;"
    df = pd.read_sql(query, connection)

    # Rename columns if needed
    df.columns = [col.lower() for col in df.columns]

    # Ensure main columns exist
    text_col = "tweet_text" if "tweet_text" in df.columns else df.columns[1]
    label_col = "label" if "label" in df.columns else df.columns[2]

    # Clean text
    df["clean_text"] = df[text_col].apply(clean_tweet_text)
    print("✅ Data cleaned successfully. Sample:")
    print(df[["clean_text", label_col]].head())

    return df
