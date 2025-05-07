<h1>🏥 Hospital Readmission Risk Predictor</h1>

<p>
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python" alt="Python" width="120"/>
  </a>
  <a href="https://flask.palletsprojects.com/">
    <img src="https://img.shields.io/badge/Flask-2.0%2B-grey?style=flat-square&logo=flask" alt="Flask" width="120"/>
  </a>
  <a href="https://scikit-learn.org/">
    <img src="https://img.shields.io/badge/scikit--learn-1.6.1-green?style=flat-square&logo=scikit-learn" alt="scikit‑learn" width="120"/>
  </a>
</p>
<p>
  <a href="https://pandas.pydata.org/">
    <img src="https://img.shields.io/badge/pandas-1.5.3-blue?style=flat-square&logo=pandas" alt="pandas" width="120"/>
  </a>
  <a href="https://numpy.org/">
    <img src="https://img.shields.io/badge/NumPy-1.25.0-lightgrey?style=flat-square&logo=numpy" alt="NumPy" width="120"/>
  </a>
</p>
<p>
  <a href="https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5">
    <img src="https://img.shields.io/badge/HTML5-E34F26-orange?style=flat-square&logo=html5" alt="HTML5" width="120"/>
  </a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/CSS">
    <img src="https://img.shields.io/badge/CSS3-1572B6-blue?style=flat-square&logo=css3" alt="CSS3" width="120"/>
  </a>
  <a href="https://fontawesome.com/">
    <img src="https://img.shields.io/badge/Font_Awesome-6.5.0-purple?style=flat-square&logo=fontawesome" alt="Font Awesome" width="120"/>
  </a>
</p>
<p>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License" width="120"/>
  </a>
</p>


This is a **Flask-based machine learning web application** that predicts whether a patient is at risk of being readmitted to the hospital. It uses a **trained Random Forest model** to provide real-time insights based on key clinical and demographic inputs.

---

## 📋 Features

- 🔘 **User‑friendly form** to capture patient details:
  - Age, Gender, Primary Diagnosis Code  
  - Number of Procedures, Days in Hospital  
  - Number of Existing Health Conditions, Discharge Code

- ⚡ **Real‑time prediction** of hospital readmission risk using a Random Forest Classifier

- 🟢🔴 **Color-coded results**:
  - 🔴 High Risk – Likely to be readmitted  
  - 🟢 Low Risk – Unlikely to be readmitted

- 📑 **Summary of patient input** for easy verification

- 🌙 **Dark-themed, responsive UI** with smooth animations and medical icons

- 🛡️ **Robust error handling** to manage missing or invalid input

- 🧩 **Modular codebase** for easy integration and customization

---

## 🧠 Machine Learning Model

- **Model Type**: Random Forest Classifier  
- **Framework**: Scikit-learn  
- **Training Data**: Historical hospital readmission dataset (not included here)  
- **Target Variable**: Binary classification (0 = No readmission, 1 = Readmitted)

The model is pre-trained and stored as a `.pkl` file (`rf_model.pkl`) located in the `/model` directory.

---

---

## 🛠️ Tech Stack

| Layer              | Technology / Library              |
| ------------------ | --------------------------------- |
| **Backend**        | Python, Flask                     |
| **ML Framework**   | scikit‑learn (RandomForestClassifier) |
| **Data Handling**  | pandas, numpy                     |
| **Frontend**       | HTML5, CSS3, Font Awesome         |
| **Deployment**     | Flask development server          |
| **Version Control**| Git, GitHub                       |

---


## 🚀 Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/Trevin07/Machine-Learning-with-Python.git
   cd Machine-Learning-with-Python/hospital-readmission-app
   ```
2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate      # macOS/Linux
   # venv\Scripts\activate     # Windows
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask app:

   ```bash
   flask run --port=5002
   ```
5. Open your browser at [http://localhost:5002](http://localhost:5002)

---

## 📸 Screenshots


  <img src="static/screenshot1.png" alt="Input Form" width="100%" />
  <img src="static/screenshot2.png" alt="Prediction Result" width="100%" />
  <img src="static/screenshot3.png" alt="Advice Section" width="100%" />
</p>

---

## 🗂 Project Structure

```
hospital-readmission-app/
├── app.py                 # Flask application
├── model/
│   └── rf_model.pkl       # Trained Random Forest model
├── static/
│   ├── styles.css         # Custom CSS
│   ├── screenshot1.png
│   ├── screenshot2.png
│   └── screenshot3.png
├── templates/
│   ├── index.html         # Input form
│   └── result.html        # Prediction results
├── requirements.txt       # Python dependencies
└── README.md              # Project overview and instructions
```

---

## ⚖️ License

This project is released under the [MIT License](https://opensource.org/licenses/MIT).

