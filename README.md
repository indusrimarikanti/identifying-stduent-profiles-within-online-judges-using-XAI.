# Identifying Student Profiles Within Online Judges Using XAI

This project analyzes student activity data from online judge platforms (such as Codeforces, LeetCode, AtCoder) and applies explainable AI (XAI) techniques to profile students and provide actionable insights for instructors.

## Features

- **Data Simulation & Ingestion**: Simulates and loads contest, submission, and problem metadata.
- **Feature Engineering**: Extracts behavioral, temporal, skill-based, and trajectory features for each student.
- **Profile Modeling**: Uses unsupervised and supervised ML for student profile classification (e.g., Novice, Improver, Specialist).
- **Explainability**: XAI techniques (SHAP/LIME) for transparent recommendations and feature attribution.
- **Dashboards**: Interactive Streamlit dashboard for students and instructors.
- **Privacy & Security**: Anonymization and access control for sensitive data.

## Project Structure

```
01_data_source.py               # Simulate and save raw data
02_etl_storage.py               # ETL pipeline and structured data storage
03_feature_engineering.py       # Feature extraction
04_modeling_explainability.py   # Modeling and XAI
05_dashboard.py                 # Streamlit dashboard
06_evaluation_feedback.py       # Evaluation and feedback loop
privacy_security.py             # Privacy and security layer
data/                           # Generated data files
```

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/indusrimarikanti/identifying-stduent-profiles-within-online-judges-using-XAI..git
   cd identifying-stduent-profiles-within-online-judges-using-XAI.
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the pipeline scripts in order**
   ```bash
   python 01_data_source.py
   python 02_etl_storage.py
   python 03_feature_engineering.py
   python 04_modeling_explainability.py
   python 06_evaluation_feedback.py
   python privacy_security.py
   streamlit run 05_dashboard.py
   ```

## Usage

- Follow the script order above to process and analyze data.
- Launch the dashboard using Streamlit for interactive visualization and insights.

## License

Specify your license (e.g., MIT, Apache-2.0) here.

## Contributing

Pull requests are welcome! For significant changes, please open an issue first to discuss what you would like to change.
