from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import numpy as np
from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

model = joblib.load('../backend/ridge_classifier.pkl')
scaler = joblib.load('../backend/scaler.pkl')

engine = create_engine(f'postgresql://postgres:{os.environ.get("postgre_password")}@localhost:5432/dementia_db')

class PatientData(BaseModel):
    gender: int
    age:int
    educ:int
    ses:int
    etiv:float
    nwbv:float
    asf:float
    mmse:int

@app.post('/predict')
def predict(data: PatientData):
    input_data = np.array([[data.gender, data.age, data.educ, data.ses, data.etiv, data.nwbv, data.asf, data.mmse]])
    input_data = scaler.transform(input_data)
    predicted = model.predict(input_data)

    with engine.connect() as conn:
        query = text("""
            insert into prediction_logs 
            (gender, age, educ, ses, etiv, nwbv, asf, mmse, predicted_cdr_result, prediction_status)
            values(:gender, :age, :educ, :ses, :etiv, :nwbv, :asf, :mmse, :result, :status)
        """)
        conn.execute(query, {
            "gender": data.gender,
            "age": data.age,
            "educ": data.educ,
            "ses": data.ses,
            "etiv": data.etiv,
            "nwbv": data.nwbv,
            "asf": data.asf,
            "mmse": data.mmse,
            "result": int(predicted),
            "status": "success"
        })
        conn.commit()

    return {"Prediction": int(predicted[0]), "status":"success"}