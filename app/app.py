from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import pandas as pd

# Load saved models
with open("models/naive_bayes_model.pkl", "rb") as nb_file:
    naive_bayes_model = pickle.load(nb_file)

with open("models/perceptron_model.pkl", "rb") as perceptron_file:
    perceptron_model = pickle.load(perceptron_file)

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    age = data['age']
    glucose = data['glucose']
    insulin = data['insulin']
    bmi = data['bmi']
    model_type = data['model']

    # Ensure you pass a DataFrame with column names as used during training
    features = pd.DataFrame([[glucose, insulin, bmi, age]], columns=['Glucose', 'Insulin', 'BMI', 'Age'])

    # Select the model based on the input
    if model_type == "naive_bayes":
        model = naive_bayes_model
    elif model_type == "perceptron":
        model = perceptron_model
    else:
        return jsonify({"error": "Invalid model type"}), 400

    # Make prediction
    prediction = model.predict(features)
    result = int(prediction[0])  # Convert the prediction to a Python integer for JSON serialization

    # Return the prediction as JSON
    return jsonify({"prediction": result})

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

