import streamlit as st

# Define conversions globally
conversions = {
    "Length": {
        "Meters": 1,
        "Kilometers": 0.001,
        "Miles": 0.000621371,
        "Feet": 3.28084
    },
    "Weight": {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274
    },
    "Temperature": {
        "Celsius": lambda x: x,
        "Fahrenheit": lambda x: (x * 9/5) + 32,
        "Kelvin": lambda x: x + 273.15
    }
}

def convert_units(value, from_unit, to_unit, category):
    if category in ["Length", "Weight"]:
        return round(value * conversions[category][to_unit] / conversions[category][from_unit], 5)
    elif category == "Temperature":
        return round(conversions[category][to_unit](value), 2)
    
    return None

st.set_page_config(page_title="Unit Converter", layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: #ffffff;
            font-family: 'Arial', sans-serif;
        }
        .stApp {
            background-color: #1e1e1e;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0px 4px 20px rgba(0, 255, 118, 0.3);
            text-align: center;
            max-width: 500px;
            margin: auto;
        }
        h1 {
            color: #00e676;
            font-weight: bold;
            text-shadow: 2px 2px 10px rgba(0, 255, 118, 0.8);
        }
        .stSelectbox, .stNumber_input, .stButton {
            width: 100%;
        }
        .stButton button {
            background: linear-gradient(45deg, #00e676, #00c853);
            color: #121212;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            transition: 0.3s;
            box-shadow: 0px 4px 10px rgba(0, 255, 118, 0.5);
        }
        .stButton button:hover {
            background: linear-gradient(45deg, #00c853, #00a544);
            transform: scale(1.05);
        }
        .stTextInput input, .stSelectbox select {
            background-color: #252525;
            color: #fff;
            border: 1px solid #00e676;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0px 4px 10px rgba(0, 255, 118, 0.2);
        }
    </style>
""", unsafe_allow_html=True)

st.title("🔄 Unit Converter")

category = st.selectbox("📌 Select a category", ["Length", "Weight", "Temperature"], key="category")
units = list(conversions[category].keys()) if category != "Temperature" else ["Celsius", "Fahrenheit", "Kelvin"]

from_unit = st.selectbox("🔹 From", units, key="from_unit")
to_unit = st.selectbox("🔸 To", units, key="to_unit")
value = st.number_input("✏️ Enter value", min_value=0.0, format="%.2f", key="value")

if st.button("🚀 Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"✅ Converted Value: {result} {to_unit}")
