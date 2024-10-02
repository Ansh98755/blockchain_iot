import datetime 
import json 
import random 
import time 
from cryptography.fernet import Fernet
def collect_data():
    temperature = round(random.uniform(20.0, 30.0), 2)
    humidity = round(random.uniform(40.0, 80.0), 2)
    timestamp = datetime.datetime.now().isoformat()
    data_point = {
        "temperature": temperature,
        "humidity": humidity,
        "timestamp": timestamp
    }
    return data_point
data = []
num_samples = 10
interval = 2
for _ in range(num_samples):
    sample = collect_data()
    data.append(sample)
    print(f"Collected sample: {sample}")
    time.sleep(interval)

with open('sensor_data.json', 'w') as file:
    json.dump(data, file, indent=4)
print('Data collection completed.')
key = Fernet.generate_key()
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)
print(f"Encryption Key: {key}")
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
fernet = Fernet(key)
with open('sensor_data.json', 'rb') as file:
    original = file.read()
encrypted = fernet.encrypt(original)
with open('sensor_data.json', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
with open('sensor_data.json', 'rb') as enc_file:
    encrypted = enc_file.read()
decrypted = fernet.decrypt(encrypted)
with open('sensor_data.json', 'wb') as dec_file:
    dec_file.write(decrypted)
