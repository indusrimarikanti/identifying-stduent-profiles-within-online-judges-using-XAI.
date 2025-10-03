import sqlite3
import pandas as pd
from datetime import datetime

def extract_features():
    conn = sqlite3.connect("data/student_profiles.db")
    submissions = pd.read_sql("SELECT * FROM submission_logs", conn)
    contests = pd.read_sql("SELECT * FROM contest_history", conn)
    problems = pd.read_sql("SELECT * FROM problem_metadata", conn)

    # Behavioral Features
    behavioral = submissions.groupby('student_id').agg(
        solved_count=('verdict', lambda x: (x == 'Accepted').sum()),
        accuracy=('verdict', lambda x: (x == 'Accepted').sum()/len(x)),
        attempts_per_problem=('attempts', 'mean')
    ).reset_index()

    # Temporal Features
    submissions['timestamp'] = pd.to_datetime(submissions['timestamp'])
    temporal = submissions.groupby('student_id').agg(
        active_days=('timestamp', lambda x: x.dt.date.nunique()),
        solve_speed=('timestamp', lambda x: ((x.max()-x.min()).days)/len(x)),
        engagement_freq=('timestamp', lambda x: len(x)/365)
    ).reset_index()

    # Skill Features
    merged = pd.merge(submissions, problems, on="problem_id")
    skill = merged.groupby('student_id')['topic'].value_counts().unstack(fill_value=0)
    skill = skill.reset_index()

    # Trajectory Features
    trajectory = contests.groupby('student_id').agg(
        rating_trend=('rating', lambda x: x.iloc[-1]-x.iloc[0] if len(x)>1 else 0),
        improvement_slope=('rating', lambda x: (x.iloc[-1]-x.iloc[0])/len(x) if len(x)>1 else 0)
    ).reset_index()

    # Merge all features
    features = behavioral.merge(temporal, on='student_id').merge(skill, on='student_id').merge(trajectory, on='student_id')
    features.to_csv("data/feature_store.csv", index=False)
    print("Step 3: Features extracted and saved to data/feature_store.csv")

if __name__ == "__main__":
    extract_features()