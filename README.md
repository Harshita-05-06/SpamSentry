# 🛡️ SpamSentry

SpamSentry is an AI-powered web application that detects whether an email is **Spam/Phishing or Safe** using Machine Learning and Natural Language Processing.

Built using **Streamlit**, it provides real-time predictions with confidence scores and risk analysis.

---

## 🚀 Live Demo

https://harshita-05-06.github.io/SpamSentry/

---

## 📌 Features

- Detects Spam / Phishing emails in real-time
- Machine Learning model (Multinomial Naive Bayes)
- Text preprocessing using NLP (TF-IDF Vectorization)
- Confidence score for predictions
- Risk score indicator
- Simple and interactive web UI using Streamlit

---

## 🧠 Tech Stack

- Python 
- Streamlit 
- Scikit-learn 
- Pandas 
- NumPy 
- NLP (TF-IDF)

---

## How It Works

1. User inputs an email
2. Text is cleaned (lowercasing, removing symbols, etc.)
3. Email is converted into numerical features using TF-IDF
4. Machine learning model predicts Spam or Safe
5. The result is displayed with a confidence score

---

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/yourusername/SpamSentry.git
cd SpamSentry
