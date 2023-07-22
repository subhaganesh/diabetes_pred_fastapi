#this code is used to create public url for our fastapi app

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import numpy as np
from sklearn.preprocessing import StandardScaler
import uvicorn
from pyngrok import ngrok
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ModelInput(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

diabetes_model = pickle.load(open('python code/diabetes_model.sav', 'rb'))
scaler = pickle.load(open('python code/scaler.sav', 'rb'))

@app.post('/diabetes_pred')
def diabetes_prediction(input_data: ModelInput):
    # Convert input_data to a dictionary
    input_dictionary = input_data.dict()

    pregnancies = input_dictionary['Pregnancies']
    glucose = input_dictionary['Glucose']
    bloodpressure = input_dictionary['BloodPressure']
    skinThickness = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    diabetesPedigreeFunction = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']

    # Create the input_list from the data
    input_list = [pregnancies, glucose, bloodpressure, skinThickness, insulin, bmi, diabetesPedigreeFunction, age]

    # Convert input_list into a 2D array with a single row
    input_array = np.array(input_list).reshape(1, -1)

    # Standardize the input data
    standardized_input = scaler.transform(input_array)

    # Make the prediction
    prediction = diabetes_model.predict(standardized_input)

    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    
ngrok_tunnel = ngrok.connect(8000)
print('Public URL:', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)