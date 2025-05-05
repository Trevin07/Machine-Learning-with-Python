# House Price Prediction

This project is a web application for predicting house prices based on various factors such as location, square footage, number of bathrooms, and number of bedrooms. The application uses machine learning (Linear Regression ,Neural Networks) to predict the price of a house given these features.

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [How to Use](#how-to-use)
- [Contributing](#contributing)
- [License](#license)

## Project Description

This project leverages a machine learning model trained on historical data about houses in Bengaluru. The model is used to predict house prices based on factors such as location, total square feet, number of bathrooms, and the number of bedrooms.

The web app uses Flask, a Python web framework, and presents a simple form to the user to input the required data. Upon submission, the app displays the predicted price of the house.

## Project Screenshot

Here is a screenshot of the application:

![Site Screenshot](static/images/SITE.jpg)

## Features

- **Location-based predictions:** Predict house prices based on the selected location.
- **Input validation:** Ensure that the user inputs valid data before submitting the form.
- **Machine Learning Model Integration:** Predicts house prices using a trained Linear Regression model.
- **User-friendly Interface:** A simple and clean user interface that allows anyone to predict house prices easily.

## Technologies Used

- **Flask**: A Python web framework used to build the web application.
- **Python**: The primary programming language for the backend.
- **scikit-learn**: A Python library for machine learning, used for the Linear Regression model.
- **HTML/CSS**: Markup and styling for the front-end user interface.
- **joblib**: Used to load the trained machine learning model.

## Setup

### Prerequisites

1. Python 3.7+
2. Flask
3. scikit-learn
4. joblib

### Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<YourGitHubUsername>/House-price-prediction.git
   cd House-price-prediction
Set up a virtual environment (Optional but recommended):

python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows

Install required dependencies:

pip install -r requirements.txt
Place the trained model file (bengaluru_home_prices_model.pkl) and the columns_list.txt file in the project directory. The trained model and columns list are essential for predictions.

Run the Flask application:

python app.py
Open your web browser and go to http://127.0.0.1:5005 to view the app.

How to Use
Open the app in your web browser.
Select a location from the dropdown menu.
Enter the total square feet of the house.
Enter the number of bathrooms.
Enter the number of bedrooms.
Click the "Predict" button to get the predicted house price.
The app will return the predicted price of the house based on the inputs provided.

Contributing
Contributions are welcome! If you want to improve the app or fix any bugs, feel free to fork the repository, make changes, and create a pull request.

To contribute, follow these steps:

Fork the repository.
Create a new branch.
Make your changes.
Push your changes to your forked repository.
Create a pull request to merge your changes into the main repository.
License
This project is open-source and available under the MIT License. See the LICENSE file for more details.Thank you!




