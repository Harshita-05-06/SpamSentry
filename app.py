import streamlit as st
import pickle
import re

model = pickle.load(open("spam_model.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))

import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


st.set_page_config(
  page_title="SpamSentry",
  page_icon="🛡️",
  layout="centered"
)

st.markdown(
    "<div style='text-align:center; font-size:80px;'>🛡️</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; font-size:18px;'>AI-powered Email Spam & Phishing Detector</p>",
    unsafe_allow_html=True
)

st.markdown("---")

email_input = st.text_area("📧 Paste your email here:", height=200)


if st.button("🔍 Analyze Email"):

    if email_input.strip() == "":
        st.warning("Please enter the email first...")
    else:

        cleaned = clean_text(email_input)
        vector = tfidf.transform([cleaned])
        prediction = model.predict(vector)[0]

        if prediction == 1:
            st.error("🚨 PHISHING EMAIL DETECTED")
            st.markdown("""
            **Why?**
            - Contains suspicious / urgent language
            - Matches phishing patterns learned by the model
            - May try to manipulate user into clicking links or sharing data
            """)
        else:
            st.success("✅ SAFE EMAIL")
            st.markdown("""
            **Why?**
            - No suspicious keywords detected
            - Normal email structure
            - Does not match phishing patterns
            """)
        
        proba = model.predict_proba(vector)[0]
        confidence = max(proba)*100

        st.markdown(f"### 🎯 Confidence: {confidence:.2f}%")
        st.progress(int(confidence))

        risk = confidence if prediction == 1 else (100 - confidence)

        st.markdown(f"### ⚠️ Risk Score: {risk:.2f}/100")
        st.progress(int(risk))



st.markdown("---")

st.markdown(
    """
    <div style='text-align:center; color:gray; font-size:14px;'>
        Made with ❤️ by <b>Harshita Ramchandani</b><br>
        SpamSentry • AI Email Protection System
    </div>
    """,
    unsafe_allow_html=True
)