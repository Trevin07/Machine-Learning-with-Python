import joblib
import numpy as np
from flask import Flask, render_template, request

# Load the pre-trained model
model = joblib.load('bengaluru_home_prices_model.pkl')

# Load the column names from the file
with open('columns_list.txt', 'r') as f:
    columns = [line.strip() for line in f.readlines()]

# Initialize the Flask app
app = Flask(__name__)

# Get the list of locations for the dropdown, removing unwanted options like "price"
locations = [col for col in columns if col not in ['total_sqft', 'bath', 'bhk', 'price']]

def predict_price(location, sqft, bath, bhk):
    # Create an array of zeros with the length of columns
    X = np.zeros(len(columns))

    # Set the features for sqft, bath, and bhk
    X[columns.index('total_sqft')] = sqft
    X[columns.index('bath')] = bath
    X[columns.index('bhk')] = bhk

    # One-hot encode the location feature
    loc_index = columns.index(location)
    X[loc_index] = 1

    # Ensure the feature array has the correct number of columns (256 features)
    if len(X) > 256:
        X = X[:256]

    # Predict the house price and return the result
    return model.predict([X])[0]

@app.route('/')
def index():
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location')
    total_sqft = float(request.form.get('total_sqft'))
    bath = int(request.form.get('bath'))
    bhk = int(request.form.get('bhk'))

    # Get the prediction based on the user's input
    prediction = predict_price(location, total_sqft, bath, bhk)

    # Render the result on the webpage
    return render_template('index.html', prediction=prediction, locations=locations)

if __name__ == '__main__':
    app.run(debug=True)
