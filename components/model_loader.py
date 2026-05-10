import joblib
import streamlit as st

MODEL_PATH = "model/chpp_model.pkl"

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()