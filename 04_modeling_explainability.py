import pandas as pd
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, silhouette_score
import shap
import matplotlib.pyplot as plt

def modeling_explainability():
    features = pd.read_csv("data/feature_store.csv")
    X = features.drop(columns=['student_id'])
    # Unsupervised: Clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    features['profile_cluster'] = kmeans.fit_predict(X)
    silhouette = silhouette_score(X, features['profile_cluster'])

    # Supervised: Classification (simulate labels)
    labels = ["Novice", "Improver", "Specialist"]
    features['profile_label'] = features['profile_cluster'].map(dict(enumerate(labels)))
    X_train, X_test, y_train, y_test = train_test_split(X, features['profile_label'], test_size=0.2, random_state=42)
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)
    f1 = f1_score(y_test, preds, average='weighted')

    # Explainability: SHAP
    explainer = shap.TreeExplainer(clf)
    shap_values = explainer.shap_values(X_test)
    plt.figure()
    shap.summary_plot(shap_values, X_test, show=False)
    plt.savefig("data/shap_summary.png")

    features.to_csv("data/model_outputs.csv", index=False)
    print(f"Step 4: Clustering silhouette={silhouette:.2f}, Classification accuracy={acc:.2f}, F1={f1:.2f}")
    print("Step 4: Model outputs and explanations saved to data/model_outputs.csv and shap_summary.png")

if __name__ == "__main__":
    modeling_explainability()