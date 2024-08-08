import streamlit as st
import json
import random
from cryptography.fernet import Fernet


def generate_data():
    temperature = round(random.uniform(-10, 40), 2)
    humidity = round(random.uniform(0, 100), 2)
    return {"temperature": temperature, "humidity": humidity}
def encrypt_data(data, key):
    fernet = Fernet(key)
    json_data = json.dumps(data).encode()
    encrypted_data = fernet.encrypt(json_data)
    return encrypted_data
def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    return json.loads(decrypted_data.decode())
def main():
    st.title("Temperature and Humidity Data Encryption")
    if st.button("Generate and Encrypt Data"):
        data = generate_data()
        st.subheader('Generated Random Data:')
        st.json(data)
        key = Fernet.generate_key()
        st.subheader('Encryption Key:')
        st.code(key.decode())
        encrypted_data = encrypt_data(data, key)
        st.subheader("Encrypted Data:")
        st.code(encrypted_data)
        decrypted_data = decrypt_data(encrypted_data, key)
        st.subheader("Decrypted Data:")
        st.json(decrypted_data)

if __name__ == "__main__":
    main()
