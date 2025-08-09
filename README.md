# Credit-Card-Fraud-Detection
# 🛡️ Fraud Detection with Isolation Forest

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange)](https://scikit-learn.org/stable/)
[![Dataset](https://img.shields.io/badge/Dataset-Kaggle-blue.svg)](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

A credit card fraud detection system using the **Isolation Forest** algorithm to detect anomalies in transactions.  
Built with Python, Pandas, and scikit-learn.

---

## 📌 Overview
This project applies **unsupervised anomaly detection** to find fraudulent credit card transactions.  
The algorithm isolates anomalies by randomly selecting features and split values — anomalies require fewer splits to isolate.

**Highlights:**
- Uses `IsolationForest` from scikit-learn.
- Works with highly imbalanced datasets.
- Evaluates with precision, recall, and F1-score.
- Simple, lightweight, and easy to deploy.

---

## 📂 Project Structure
Fraud-Detection/
│
├── app.py # Optional web app script
├── fraud_detection.py # Main model training & evaluation script
├── creditcard.csv # Dataset (add manually)
└── README.md # Documentation
