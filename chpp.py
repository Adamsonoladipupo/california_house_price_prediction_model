import streamlit as st

from components.sidebar import sidebar
from components.prediction_form import prediction_form
from components.result_card import display_prediction
from components.predictor import predict_house_price

st.set_page_config(
    page_title="CHPP",
    layout="wide"
)
st.title("California House Price Predictor")
sidebar()
st.write("Predict housing prices in California using our model")
input_data = prediction_form()
if st.button("Predict House Price"):
    try:
        prediction = predict_house_price(input_data)
        display_prediction(prediction)
    except Exception as error:
        st.error(f"Prediction Failed: {error}")


