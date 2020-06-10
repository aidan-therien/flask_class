import requests

r = requests.get("http://127.0.0.1:5000/")
answer = r.json()
print(answer["calc_info"])

out_json = {"age": 30, "height_in": 60, "gender": "male"}
r = requests.post("http://127.0.0.1:5000/iwc", json = out_json)
print(r.json())