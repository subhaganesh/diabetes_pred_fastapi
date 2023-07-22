import json
import requests

#url='https://6781-34-86-158-158.ngrok.io/diabetes_pred'  # this is used for public url 
url='http://127.0.0.1:8000/diabetes_pred'

input_data_for_model= {
    'Pregnancies' : 1,
    'Glucose' : 103,
    'BloodPressure' : 30,
    'SkinThickness' : 38,
    'Insulin' : 83,
    'BMI' : 43.3,
    'DiabetesPedigreeFunction' : 0.183,
    'Age' : 33
    }

input_json=json.dumps(input_data_for_model)

response= requests.post(url, data=input_json)

print(response.text)