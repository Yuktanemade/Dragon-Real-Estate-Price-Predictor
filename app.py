import streamlit as st
import numpy as np
import joblib
import base64

# Color theme
color_palette = {
    "dark_blue": "#2c3e50",
    "hot_pink": "#ef476f",
    "mint_green": "#06d6a0",
    "input_text": "#000000",
    "input_bg": "#ffffff",
    "input_border": "#2c3e50",
    "input_focus": "#ef476f50"
}

# Background setup
def set_background(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
    st.markdown(f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');
        html, body, [class*="css"] {{
            font-family: 'Poppins', sans-serif;
            font-size: 19px;
            color: {color_palette['dark_blue']};
        }}
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-attachment: fixed;
        }}
        h1, h2, h3 {{
            color: {color_palette['dark_blue']} !important;
            font-weight: 700;
        }}
        label, .stSliderLabel, .stNumberInput label {{
            font-weight: 700 !important;
            color: {color_palette['dark_blue']} !important;
            font-size: 18px !important;
        }}
        .stTextInput > div > div > input,
        .stNumberInput input,
        .stSelectbox div div div,
        .stSlider > div > div > div {{
            background-color: {color_palette['input_bg']} !important;
            color: {color_palette['input_text']} !important;
            font-size: 17px !important;
            font-weight: 600;
            border: 2px solid {color_palette['input_border']} !important;
            border-radius: 10px;
            padding: 6px 10px;
        }}
        input:focus, select:focus {{
            outline: none !important;
            border-color: {color_palette['hot_pink']} !important;
            box-shadow: 0 0 10px {color_palette['input_focus']};
        }}
        .stButton > button {{
            background-color: {color_palette['hot_pink']};
            color: white;
            font-size: 18px;
            font-weight: 700;
            border-radius: 10px;
            padding: 10px 20px;
        }}
        .stSuccess {{
            color: {color_palette['mint_green']} !important;
            font-size: 22px;
            font-weight: bold;
        }}
        </style>
    """, unsafe_allow_html=True)

# Page setup
st.set_page_config(page_title="Dragon Real Estate Price Predictor", layout="centered")
set_background("background.jpg")

# Load model
model = joblib.load("Dragon.joblib")

st.title("Dragon Real Estate Price Predictor")
user_name = st.text_input("Enter your name:")

if user_name:
    st.markdown(f"## Welcome, **{user_name}**!")
    st.markdown("### Fill in the 13 features below to predict your house price:")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<span style='font-size:22px; font-weight:bold; color:#2c3e50;'>CRIM - Per capita crime rate</span>", unsafe_allow_html=True)
        CRIM = st.number_input("", 0.0, 100.0, step=0.1)

        st.markdown("<span style='font-size:22px; font-weight:bold; color:#2c3e50;'>ZN - Residential zone %</span>", unsafe_allow_html=True)
        ZN = st.number_input("", 0.0, 100.0, step=1.0)

        st.markdown("<span style='font-size:22px; font-weight:bold; color:#2c3e50;'>INDUS - Non-retail acres</span>", unsafe_allow_html=True)
        INDUS = st.number_input("", 0.0, 30.0, step=0.1)

        st.markdown("<span style='font-size:22px; font-weight:bold; color:#2c3e50;'>CHAS - Bounds river?</span>", unsafe_allow_html=True)
        CHAS = st.selectbox("", [0, 1])

        st.markdown("<span style='font-size:22px; font-weight:bold; color:#2c3e50;'>NOX - NO concentration</span>", unsafe_allow_html=True)
        NOX = st.number_input("", 0.0, 1.0, step=0.01)

        st.markdown("<span style='font-size:22px; font-weight:bold; color:#2c3e50;'>RM - Rooms per dwelling</span>", unsafe_allow_html=True)
        RM = st.slider("", 3.0, 9.0, step=0.1)

        st.markdown("<span style='font-size:22px; font-weight:bold; color:#2c3e50;'>AGE - Old buildings %</span>", unsafe_allow_html=True)
        AGE = st.slider("", 0.0, 100.0, step=1.0)

    with col2:
        st.markdown("<span style='font-size:22px; font-weight:bold; color:#2c3e50;'>DIS - Distance to work centers</span>", unsafe_allow_html=True)
        DIS = st.number_input("", 0.0, 15.0, step=0.1)

        st.markdown("<span style='font-size:22px; font-weight:bold; color:#2c3e50;'>RAD - Highway access index</span>", unsafe_allow_html=True)
        RAD = st.number_input("", 1.0, 24.0, step=1.0)

        st.markdown("<span style='font-size:22px; font-weight:bold; color:#2c3e50;'>TAX - Property tax rate</span>", unsafe_allow_html=True)
        TAX = st.number_input("", 100.0, 800.0, step=1.0)

        st.markdown("<span style='font-size:22px; font-weight:bold; color:#2c3e50;'>PTRATIO - Student-teacher ratio</span>", unsafe_allow_html=True)
        PTRATIO = st.number_input("", 10.0, 25.0, step=0.1)

        st.markdown("<span style='font-size:22px; font-weight:bold; color:#2c3e50;'>B - Proportion of Black people</span>", unsafe_allow_html=True)
        B = st.number_input("", 0.0, 400.0, step=1.0)

        st.markdown("<span style='font-size:22px; font-weight:bold; color:#2c3e50;'>LSTAT - % lower status population</span>", unsafe_allow_html=True)
        LSTAT = st.number_input("", 0.0, 40.0, step=0.1)

    st.markdown("---")

    if st.button("Predict House Price"):
        input_data = np.array([[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS,
                                RAD, TAX, PTRATIO, B, LSTAT]])
        raw_price = model.predict(input_data)[0]
        modern_price = raw_price * 1000 * 10   # Example scale
        dollar_price = modern_price / 100      # Convert to USD approx

        st.markdown(
            f"<h4 style='color:#0077b6; font-weight:bold;'>💲 Predicted House Price for {user_name}: ${dollar_price:,.2f}</h4>",
            unsafe_allow_html=True
        )
        st.balloons()
