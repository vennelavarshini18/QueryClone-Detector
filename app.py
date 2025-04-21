import streamlit as st
import helper
import pickle
from nltk.corpus import stopwords

# Ensure you've downloaded the stopwords first
import nltk
nltk.download('stopwords')

# Save the stopwords list
with open("stopwords.pkl", "wb") as f:
    pickle.dump(stopwords.words('english'), f)

model = pickle.load(open('model.pkl','rb'))

st.set_page_config(page_title="Duplicate Question Detector", layout="centered")
st.markdown("<h1 style='text-align: center; color: #6c63ff;'>Duplicate Question Pairs Detector 🤖</h1>", unsafe_allow_html=True)
st.write("Enter two questions to check if they are duplicates or not using a trained ML model.")

q1 = st.text_input('🔹 Enter Question 1')
q2 = st.text_input('🔸 Enter Question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')
with st.sidebar:
    st.image("https://miro.medium.com/v2/resize:fit:602/1*eNseZEXViToel_oC_vfSzQ.png", caption="quora", use_container_width=True)
    st.markdown("### 📌 About")
    st.write("""
    This tool uses a machine learning model to detect whether two input questions are semantically similar (i.e., duplicates).
    - Based on Quora dataset
    - Preprocessed via `helper.query_point_creator`
    """)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>Made using Streamlit | Github</p>", unsafe_allow_html=True)
