import pickle
import numpy as np
import pandas as pd
import streamlit as st

# load the house price prediction model
loaded_model = pickle.load(open("HousePrediction.pkl", 'rb'))

# Streamlit app
st.title("House Price Prediction")

# User input for prediction
st.header("Enter Details")

def input_values():
    HouseAge = st.number_input("Year")
    Bedroom = st.number_input("Number of Bedrooms")
    FullBath = st.number_input("Number of Bathrooms")
    LotArea = st.number_input("Area (in sq ft)")
    Location = st.selectbox("Location", ['Urban', 'SubUrban', 'Rural'])

    # change the inputs to pandas dataframe
    values = {'HouseAge': [HouseAge], 'Bedroom':[Bedroom], 'FullBath':[FullBath], 'LotArea':[LotArea], 'Location': [Location]}
    values = pd.DataFrame(values)

    # preprocessing
    location = {'Rural':0, 'SubUrban':1, 'Urban':2}
    values['HouseAge'] = 2024 - values['HouseAge'][0]
    values['Location'] = location[values['Location'][0]]

    return values

def main():
    parameters = input_values()
    # Make prediction
    if st.button("Predict"):
        prediction = loaded_model.predict(parameters)
        st.write(f"Predicted House Price: ${prediction[0]:,.2f}")

if __name__ == "__main__":
    main()