![image](https://d2jx2rerrg6sh3.cloudfront.net/images/Article_Images/ImageForArticle_22744_16565132428524067.jpg)
# diabetes fastapi project
The "Diabetes FastAPI Project" is a web application built using the FastAPI framework and Python. Its main purpose is to provide a simple API for predicting whether a person is diabetic or not based on input features such as medical measurements and age. The model used for prediction is a machine learning model trained on a dataset of diabetes-related information.

## The project consists of the following components:

*FastAPI Framework: FastAPI is a modern, fast, web framework for building APIs with Python. It provides automatic validation of request data, automatic generation of API documentation (using OpenAPI and JSON Schema), and easy integration with asynchronous code for handling high loads efficiently.

*Machine Learning Model: The project includes a trained machine learning model (e.g., logistic regression, random forest, etc.) that can predict the likelihood of diabetes based on input features. The model is loaded into the application using the pickle library, which allows for deserialization and usage in real-time predictions.

*Data Preprocessing: Before making predictions, the input data is preprocessed to ensure it's in a suitable format for the model. This includes converting the input data into a standardized format using the scikit-learn library's StandardScaler.

*API Endpoint: The FastAPI application exposes an API endpoint (/diabetes_pred) that accepts HTTP POST requests containing input data in JSON format. Users can send a POST request to this endpoint with their input data, and the application will respond with the predicted outcome: either "The person is not diabetic" or "The person is diabetic."

*Pydantic Model Validation: To ensure that the input data adheres to the correct data types and structure, the project uses Pydantic's BaseModel to create a data model representing the expected input.

Overall, the "Diabetes FastAPI Project" is a user-friendly and efficient web application that utilizes machine learning to predict diabetes risk based on user-provided data. It can be deployed on a server and accessed through API requests, making it suitable for integration with various applications, including web and mobile platforms.

## How to use this project for prediction 
Download the files and go to command prompt

*cd <your path for project>
*uvicorn <file_name>:app  (instance name, here the instance is app)

run this above two commands a local host will be created ,localhost/docs 
