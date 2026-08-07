import joblib
import streamlit as st

MODEL_PATH = "model/best_model_v1.pkl"

def load_model():
    return joblib.load(MODEL_PATH)

model = load_model()