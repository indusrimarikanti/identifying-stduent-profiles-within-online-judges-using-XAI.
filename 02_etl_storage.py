import pandas as pd
import sqlite3
import hashlib
import os

os.makedirs("data", exist_ok=True)

def anonymize_student_id(student_id):
    return hashlib.sha256(student_id.encode()).hexdigest()

def clean_and_store():
    submissions = pd.read_csv("data/submission_logs.csv")
    contests = pd.read_csv("data/contest_history.csv")
    problems = pd.read_csv("data/problem_metadata.csv")

    # Clean: anonymize student_id, normalize tags
    submissions['student_id'] = submissions['student_id'].apply(anonymize_student_id)
    contests['student_id'] = contests['student_id'].apply(anonymize_student_id)
    # tags already normalized as comma string

    # Store in SQLite
    conn = sqlite3.connect("data/student_profiles.db")
    submissions.to_sql("submission_logs", conn, if_exists="replace", index=False)
    contests.to_sql("contest_history", conn, if_exists="replace", index=False)
    problems.to_sql("problem_metadata", conn, if_exists="replace", index=False)
    conn.close()
    print("Step 2: Data cleaned and stored in data/student_profiles.db")

if __name__ == "__main__":
    clean_and_store()