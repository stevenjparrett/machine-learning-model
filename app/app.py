# app/app.py
from flask import Flask, request, render_template
import sys
import os

# Ensure the src directory is in the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.model import predict_next_day_close

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    stock = request.form['stock']
    if stock: 
        prediction = predict_next_day_close(stock)
        if prediction is None:
            prediction = "Data not available."
    else:
        prediction = "Please enter a valid stock ticker."
    return render_template('result.html', stock=stock, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
