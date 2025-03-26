import streamlit as st 

def convert_units(value, unit_from, unit_to):

    conversions = {
        "meters_kilometers" : 0.001,  # 1 meter = 0.001 kilometer
        "kilometers_meters" : 1000,   # 1 kilometer = 1000 meter
        "grams_kilograms" : 0.001,  # 1 gram = 0.001 kilograms
        "kilograms_grams" : 1000,    # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}" # generate a key based on the input and output units

    if key in conversions:
        conversions = conversions[key]
        return value * conversions 
    else:
        return "conversion not supported" 
    
st.title("Unit Convertor")    

value = st.number_input("Enter the value:")

unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])

unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted value:{result}")