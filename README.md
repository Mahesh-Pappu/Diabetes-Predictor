# Machine Learning-Based Diabetes Prediction System

## Overview
This project is a web-based application that predicts diabetes type using two machine learning models: **Gaussian Naive Bayes** and **Perceptron**. The system provides a dynamic interface for users to input features such as age, glucose level, insulin level, and BMI and displays real-time predictions. The application is built using Python, Flask, and JavaScript.

---

## Features
- **Machine Learning Models:**  
  - Gaussian Naive Bayes: A probabilistic model based on Bayes' theorem.
  - Perceptron: A linear classifier implemented with gradient-based updates.
  
- **Web Interface:**  
  - User-friendly frontend built with HTML and JavaScript.
  - Real-time predictions via asynchronous API calls using Fetch.

- **Flask Backend:**  
  - Serves both machine learning models via a `/predict` API endpoint.
  - Enables users to select which model to use for predictions.

- **Performance Analysis:**  
  - Evaluated both models using k-fold cross-validation.
  - Compared performance metrics: accuracy, precision, recall, and F1-score.

---

## Installation and Setup

### Prerequisites
- Python 3.x
- Flask
- Required Python libraries (see `requirements.txt`)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>


2. Run the Flask backend:
   ```bash
   python app.py
