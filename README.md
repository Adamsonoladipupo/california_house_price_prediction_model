# CHPP — California House Price Predictor

CHPP (California House Price Predictor) is a machine learning web application that predicts house prices in California using user-provided features. The project uses a trained Scikit-learn model and a Streamlit-based frontend for interaction.

---

## Project Overview

Users input housing features such as income level, house age, number of rooms, population, and geographic location. The app then returns a predicted house price instantly.

### System Flow

User → Streamlit Frontend → ML Model (Scikit-learn Pipeline) → Prediction Result

---

## Machine Learning Model

- Built using **Scikit-learn**
- Trained in Jupyter/IPython notebook
- Uses a **Pipeline** for preprocessing + prediction
- Saved using **Joblib**
- Stored at: `model/model.pkl`

---

## 🛠 Tech Stack

- Python 3.10+
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib
- UV (package manager)

---

## Project Structure

