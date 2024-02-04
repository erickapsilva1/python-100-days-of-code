import json
with open("data.json", mode="r") as file:
    data = json.load(file)

    for key, value in data.items():
        if key == "Amazon":
            print(key, value)
            print(value['password'])