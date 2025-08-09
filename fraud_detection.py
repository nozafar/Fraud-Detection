# fraud_detection.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report

# Load data
df = pd.read_csv("creditcard.csv")

# Features & target
X = df.drop("Class", axis=1)
y = df["Class"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = IsolationForest(contamination=0.001, random_state=42)
model.fit(X_train)

# Predictions
y_pred = model.predict(X_test)
y_pred = [1 if p == -1 else 0 for p in y_pred]

print(classification_report(y_test, y_pred))
