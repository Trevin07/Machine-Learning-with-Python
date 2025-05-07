from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model/rf_model.pkl', 'rb'))

# Initialize label encoders and fit with known categories
gender_encoder = LabelEncoder()
diagnosis_encoder = LabelEncoder()
discharge_encoder = LabelEncoder()

gender_encoder.fit(['Male', 'Female'])
diagnosis_encoder.fit(['Heart Disease', 'COPD', 'Diabetes', 'Kidney Disease', 'Hypertension'])
discharge_encoder.fit(['Home Health Care', 'Rehabilitation Facility', 'Skilled Nursing Facility', 'Home'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # 1) Capture raw inputs for display
    raw_age               = request.form.get('age')
    raw_gender            = request.form.get('gender')
    raw_diag              = request.form.get('primary_diagnosis')
    raw_num               = request.form.get('num_procedures')
    raw_days              = request.form.get('days_in_hospital')
    raw_comorbidity_score = request.form.get('comorbidity_score')
    raw_discharge_to      = request.form.get('discharge_to')

    # 2) Convert & encode for model
    try:
        age               = int(raw_age)
        gender            = gender_encoder.transform([raw_gender])[0]
        diagnosis         = diagnosis_encoder.transform([raw_diag])[0]
        num_procedures    = int(raw_num)
        days_in_hospital  = int(raw_days)
        comorbidity_score = int(raw_comorbidity_score)
        discharge_to      = discharge_encoder.transform([raw_discharge_to])[0]
    except Exception:
        # on any error, still render template (with no details)
        return render_template('result.html',
                               result="Input Error: Please check your data.",
                               age=raw_age, gender=raw_gender, primary_diagnosis=raw_diag,
                               num_procedures=raw_num, days_in_hospital=raw_days,
                               comorbidity_score=raw_comorbidity_score, discharge_to=raw_discharge_to)

    # 3) Build DataFrame & predict
    input_data = pd.DataFrame([{
        'age': age,
        'gender': gender,
        'primary_diagnosis': diagnosis,
        'num_procedures': num_procedures,
        'days_in_hospital': days_in_hospital,
        'comorbidity_score': comorbidity_score,
        'discharge_to': discharge_to
    }])

    prediction = model.predict(input_data)[0]
    result = 'LIKELY TO BE READMITTED' if prediction == 1 else 'UNLIKELY TO BE READMITTED'

    # 4) Render with both result and raw inputs
    return render_template('result.html',
                           result=result,
                           age=raw_age,
                           gender=raw_gender,
                           primary_diagnosis=raw_diag,
                           num_procedures=raw_num,
                           days_in_hospital=raw_days,
                           comorbidity_score=raw_comorbidity_score,
                           discharge_to=raw_discharge_to)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
