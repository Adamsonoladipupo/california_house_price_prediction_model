import streamlit as st


def sidebar():
    with st.sidebar:
        st.title("CHPP")

        st.markdown("""
        CHPP predicts housing prices in California using machine learning.

        ### Tech Stack
        - Python
        - Streamlit
        - Scikit-learn
        - Pandas
        - Joblib

        ### Model

        Trained using California housing data.
        """)
        st.markdown(
            '<a href="https://www.kaggle.com/code/ahmedmahmoud16/california-housing-prices?select=housing.csv">Get Dataset</a>',
            unsafe_allow_html=True
        )

        st.divider()
        st.markdown(
            '<a href="https://github.com/Adamsonoladipupo/">Created by Adamson</a>',
            unsafe_allow_html=True
        )
