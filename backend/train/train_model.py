"""
Train a simple classifier on Iris and save using joblib.
Run:
    python train_model.py
"""
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent.parent / 'model.joblib'

def main():
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Test accuracy: {acc:.4f}")

    joblib.dump(clf, MODEL_PATH)
    print(f"Saved model to {MODEL_PATH}")

if __name__ == '__main__':
    main()