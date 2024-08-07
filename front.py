import streamlit as st
import json

def load_file_data(filename):
    with open(filename, "r") as json_file:
        return json.load(json_file)
filename='weatherr.json'
weather_data=load_file_data(filename)
st.title('Random Temprature and Humidity values')
st.header('Generated Random data = ')
for i, data in enumerate(weather_data, start=1):
    st.write(f"Record {i}:")
    st.write(f"Temperature: {data['temprature']} °C")
    st.write(f"Humidity: {data['humidity']} %")
    st.write("---")