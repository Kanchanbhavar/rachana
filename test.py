# import requests
# BASE_URL='http//:127.0.0:8000/'
# ENDPOINT='apijson1'
# resp=requests.get(BASE_URL+ENDPOINT)
# print(resp.json())
# data=resp.json
# print('data from django application')
# print('#'*50)
# print("Employee Number:",data['eno'])
# print("Employee Name:",data['ename'])
# print("Employee Sallary:",data['esal'])
# print("Employee Address:",data['eaddr'])


#for class base view json response from django application
import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='jsoncbv'
resp=requests.get(BASE_URL+ENDPOINT)
#print(resp.json())
data=resp.json()
print(data)