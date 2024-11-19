import streamlit as st
import time
from datetime import datetime

blockchain = Blockchain()

st.title("IoT Sensor Data on Blockchain")
st.sidebar.header("Sensor Input")
temperature = st.sidebar.number_input("Temperature (°C)", step=0.1)
humidity = st.sidebar.number_input("Humidity (%)", step=1)

if st.sidebar.button("Add Sensor Data"):
    sensor_data = {"temperature": temperature, "humidity": humidity}
    blockchain.add_block(sensor_data)
    st.sidebar.success("Sensor data added to blockchain.")

st.header("Blockchain")
for block in blockchain.chain:
    with st.expander(f"Block {block.index}"):
        st.write(f"Timestamp: {datetime.fromtimestamp(block.timestamp)}")
        st.write(f"Sensor Data: {block.sensor_data}")
        st.write(f"Hash: {block.hash}")
        st.write(f"Previous Hash: {block.previous_hash}")

if st.button("Validate Blockchain"):
    if blockchain.is_chain_valid():
        st.success("Blockchain is valid.")
    else:
        st.error("Blockchain is invalid!")
