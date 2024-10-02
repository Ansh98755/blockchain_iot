# import json
# import random
# def weather():
#     temprature=round(random.uniform(-30,50),2)
#     humidity=round(random.uniform(1,100),2)
#     return{
#         "temp":temprature,
#         "humid":humidity
#     }
# num=10
# filename="weat.json"
# weather_data=[weather() for _ in range(num)]
# with open(filename,"w") as json_file:
#     json.dump(weather_data,json_file,indent=4)
# print("Weather data has been written " + filename)

# num=100
# k=num/2
# def is_prime():
#     for i in range(2,int(k)):
#         if(num%i)==0:
#             print("The given number is not a prime no")
#             return
#     print("The given the number is a prime no.")
#     return
# is_prime()

#prime numbers upto 10
# def is_prime():
#     for i in range(2,11):
#         count=0
#         for j in range(2,i):
#             if(i%j)==0:
#                 print('The number' + str(i) + ' is not a prime number')
#                 count=1
#                 break
#         if count!=1:
#             print('The number' + str(i) + 'is a prime number')

#     return
# is_prime()
#sieve of eratosthenes
# num=25
# prime_elments=['True']*(num+1)
# prime_elments[0]=prime_elments[1]='False'
# def is_prime():
#     for i in range(2,20):
#         prime_elments[i]='True'
#         for j in range(i*i,num+1,i):
#             prime_elments[j]='False'
#     for i in range(num+1):
#         if(prime_elments[i]=='True'):
#             print(i)
# is_prime()


#collect the random data for temprature and humidity and store it in the json file

# import json 
# import random
# def weather_data():
#     temprature=round(random.uniform(-50,30),2)
#     humidity=round(random.uniform(1,100),2)
#     return{
#         "temprature":temprature,
#         "humidity":humidity
#     }
# num=10
# filename="data.json"
# weather_data_values=[weather_data() for _ in range(num)]
# with open(filename,"w") as json_file:
#     json.dump(weather_data_values,json_file,indent=4)
# print(f'Data has been written to {filename}')
#sieve of eratosthenes

# num=30
# is_prime=['True']*(num+1)
# is_prime[0]=is_prime[1]='False'
# def check_prime():
#     for i in range(2,num):
#         if is_prime[i]=='True':
#             for j in range(i*i,num+1,i):
#                 is_prime[j]='False'
#     for i in range(2,num+1):
#         if(is_prime[i]=='True'):
#             print(f'The number {i} is a prime number')
# check_prime()

#encryption and decryption of data using rsa and generating public and private key
# from cryptography.hazmat.primitives.asymmetric import rsa,padding
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.backends import default_backend

# private_key=rsa.generate_private_key(
#     public_exponent=65537,
#     key_size=2048,
#     backend=default_backend
# )

# public_key=private_key.public_key()
# message=b'Hey, there i\'m Ayush Mehendiratta'

# encrypted_message = public_key.encrypt(
#     message,
#     padding.OAEP(
#         mgf=padding.MGF1(algorithm=hashes.SHA256()),
#         algorithm=hashes.SHA256(),
#         label=None
#     )
# )
# print(f'Encrypted Message = {encrypted_message}')
# decrypted_message=private_key.decrypt(
#     encrypted_message,
#     padding.OAEP(
#         mgf=padding.MGF1(algorithm=hashes.SHA256()),
#         algorithm=hashes.SHA256(),
#         label=None
#     )
# )
# print(f'The decrypted form of the encrypted message = {decrypted_message.decode('utf-8')}')
import datetime
import json
import random
import time 
from cryptography.fernet import Fernet
def collect_data():
    temprature=round(random.uniform(-30,50),2)
    humidity=round(random.uniform(1,100),2)
    timestamp=datetime.datetime.now().isoformat()
    data_return={
        "temprature": temprature,
        "humidity": humidity,
        "timestamp": timestamp
    }
    return data_return 
data=[]
interval=2
num_samples=10

for _ in range(num_samples):
    sample=collect_data()
    data.append(sample)
    print(f'Collected Samples : {sample}')
    time.sleep(interval)
with open('Sensor_data.json', 'w') as file:
    json.dump('Sensor_data.json',file, indent=4)
print('Data collection completed')
key=Fernet.generate_key()
with open('filekey.key' ,'wb') as filekey:
    filekey.write(key)
print(f'Encryption key = {key}')
with open('filekey.key' , 'rb') as filekey:
    key=filekey.read()
fernet=Fernet(key)
with open('Sensor_data.json' , 'rb') as file:
    original=file.read()
encrypted=fernet.encrypt(original)
with open('Sensor_data.json','wb') as file:
    file.write(encrypted)
with open('Sensor_data.json', 'rb') as enc_file:
    encry=enc_file.read()
decrypted=fernet.decrypt(encry)
with open('Sensor_data.json','wb') as dec_file:
    dec_file.write(decrypted)