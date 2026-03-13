import requests

response = requests.get('https://dummyjson.com/users')
print(response.status_code)  # Output: 200
#print(response.json())  # Output: JSON response from the API

idsuo40=[]
for i in response.json()['users']:
    print(i)
    print("-----------------------------")


