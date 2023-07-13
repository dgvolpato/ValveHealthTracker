import json

print("GET pressure request")
f = open("backend/app/sample_pressure_input.json", "r")
sample_json_file = json.load(f)
# sample_json_file = {"hello": "world"}
valve_pressure_history = sample_json_file
f.close()
print("response: ", valve_pressure_history)