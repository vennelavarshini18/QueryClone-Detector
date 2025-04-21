import streamlit as st
import helper
import pickle
from nltk.corpus import stopwords

import nltk
nltk.download('stopwords')
with open("stopwords.pkl", "wb") as f:
    pickle.dump(stopwords.words('english'), f)

model = pickle.load(open('model.pkl','rb'))

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')

st.image("https://miro.medium.com/v2/resize:fit:602/1*eNseZEXViToel_oC_vfSzQ.png", caption="Sunrise by the mountains" , width=300)
