import requests

r = requests.get("http://127.0.0.1:5000/time")
answer = r.json()
print(answer)

out_json = {"date": "10/10/1998", "units": "years"}
r = requests.post("http://127.0.0.1:5000/age", json = out_json)
print(r.json())