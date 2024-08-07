import json
import random

def weather():
    temprature=round(random.uniform(-30,50),2)
    humidity=round(random.uniform(1,100),2)
    return{
        "temprature":temprature,
        "humidity":humidity
    }
num=10
weather_data=[weather() for _ in range(num)]
filename='weatherr.json'
with open(filename,"w")as json_file :
    json.dump(weather_data,json_file,indent=6)

print("Weather data has been written to the " +filename+ "file")
