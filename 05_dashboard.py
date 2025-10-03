import streamlit as st
import pandas as pd
import os

if not os.path.exists("data/model_outputs.csv"):
    st.error("Run previous steps to generate model_outputs.csv.")
else:
    features = pd.read_csv("data/model_outputs.csv")

    st.title("Student Profiling Dashboard")

    student_ids = features['student_id'].tolist()
    selected_id = st.selectbox("Select Student", student_ids)

    student = features[features['student_id'] == selected_id].iloc[0]
    st.header(f"Profile: {student['profile_label']}")
    st.write("Top Features:")
    for col in features.columns:
        if col not in ['student_id', 'profile_label', 'profile_cluster']:
            st.write(f"{col}: {student[col]}")

    st.subheader("Progress Timeline (simulated)")
    st.line_chart([student['rating_trend'], student['improvement_slope']])

    st.subheader("Cohort Distribution")
    st.bar_chart(features['profile_label'].value_counts())

    st.subheader("Instructor Insights")
    skill_cols = ["DP", "Graphs", "Greedy", "Math", "Strings"]
    weak_areas = [c for c in skill_cols if c in features.columns and features[c].mean() < 5]
    if weak_areas:
        st.write(f"Common weak areas: {', '.join(weak_areas)}")
    else:
        st.write("No significant weak areas detected.")

    st.subheader("Early Warning System")
    plateaued = features[features['improvement_slope'] < 0.1]
    st.write(f"Plateaued learners: {len(plateaued)}")