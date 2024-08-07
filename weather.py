import json
import random

def generate_weather_data():
    temperature = round(random.uniform(-30, 50), 2)
    humidity = round(random.uniform(0, 100), 2)
    return {
        "temperature": temperature,
        "humidity": humidity
    }

num = 10
weather_data_list = [generate_weather_data() for _ in range(num)]

filename = 'weather_data.json'
with open(filename, "w") as json_file:
    json.dump(weather_data_list, json_file, indent=4)

print(f"Weather data has been written to '{filename}'.")
