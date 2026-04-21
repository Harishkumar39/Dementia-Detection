import os

import requests
import streamlit as st

st.title("Detection of dementia")
st.write("Enter patient details to predict dementia status")

gender = st.selectbox("Gender", options=[0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
age = st.number_input("Age", min_value=1, max_value=120)
educ = st.number_input("Education", min_value=0, max_value=age)
ses = st.number_input("Socioeconomic Status 1>5", min_value=1, max_value=5)
etiv = st.number_input("eTIV", min_value=1, max_value=2500)
nwbv = st.number_input("nWBV", min_value=0.0, max_value=1.0)
asf = st.number_input("ASF", min_value=0.0, max_value=2.0)
mmse = st.number_input("MMSE", min_value=0, max_value=30)

if st.button("Predict"):
    payload = {
        "gender":gender,
        "age":age,
        "educ":educ,
        "ses":ses,
        "etiv":etiv,
        "nwbv":nwbv,
        "asf":asf,
        "mmse":mmse
    }
    try:
        url = os.environ.get("BACKEND_URL", "http://127.0.0.1:8003")
        response = requests.post(f"{url}/predict", json=payload)

        if response.status_code == 200:
            result = response.json()
            prediction = result['Prediction']
            if prediction == 0:
                st.success("Non-Demented")
            elif prediction == 1:
                st.error("Mildly Demented")
            elif prediction == 2:
                st.error("Moderately Demented")
            else:
                st.error("Severly Demented")
    except Exception as e:
        st.error(f"Couldn't connect to backend: {e}")


