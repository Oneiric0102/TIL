import json

with open("password.json",'r') as f:
    json_data = json.load(f)

print(json_data["password"])
json_data["delivery"] = "만두"

with open("password.json",'w') as f:
    json.dump(json_data,f, ensure_ascii=False)