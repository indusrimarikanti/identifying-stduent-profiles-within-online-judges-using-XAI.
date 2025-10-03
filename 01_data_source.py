import pandas as pd
import random
from datetime import datetime, timedelta
import os

os.makedirs("data", exist_ok=True)

# Simulate student submission logs
def simulate_submission_logs(num_students=50, num_problems=100):
    logs = []
    for sid in range(1, num_students+1):
        for pid in random.sample(range(1, num_problems+1), random.randint(10, 60)):
            log = {
                "student_id": f"user_{sid}",
                "problem_id": pid,
                "verdict": random.choice(["Accepted", "Wrong Answer", "Time Limit Exceeded"]),
                "attempts": random.randint(1, 5),
                "timestamp": (datetime.now() - timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d %H:%M:%S"),
            }
            logs.append(log)
    return pd.DataFrame(logs)

# Simulate contest participation history
def simulate_contest_history(num_students=50, num_contests=20):
    history = []
    for sid in range(1, num_students+1):
        for cid in range(1, num_contests+1):
            record = {
                "student_id": f"user_{sid}",
                "contest_id": cid,
                "rating": random.randint(1200, 2500),
                "rank": random.randint(1, 100),
                "score": random.uniform(0, 100),
            }
            history.append(record)
    return pd.DataFrame(history)

# Simulate problem metadata
def simulate_problem_metadata(num_problems=100):
    difficulties = ["Easy", "Medium", "Hard"]
    tags = ["DP", "Graphs", "Greedy", "Math", "Strings"]
    metadata = []
    for pid in range(1, num_problems+1):
        record = {
            "problem_id": pid,
            "difficulty": random.choice(difficulties),
            "tags": ",".join(random.sample(tags, random.randint(1, 3))),
            "topic": random.choice(tags),
        }
        metadata.append(record)
    return pd.DataFrame(metadata)

if __name__ == "__main__":
    submissions = simulate_submission_logs()
    contests = simulate_contest_history()
    problems = simulate_problem_metadata()

    submissions.to_csv("data/submission_logs.csv", index=False)
    contests.to_csv("data/contest_history.csv", index=False)
    problems.to_csv("data/problem_metadata.csv", index=False)
    print("Step 1: Data simulated and saved to data/*.csv")