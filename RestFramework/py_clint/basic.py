import requests

endpoint = " http://127.0.0.1:8000/api/create/"
response = requests.post(endpoint, json={
    "name": "Life3",
    "age": 20,
    "gender": "M"
})
# print(response.text)


print(response.json())
# print(dir(response.data))

print(response.status_code)
