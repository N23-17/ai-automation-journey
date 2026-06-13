from pathlib import Path
import json

current_file = Path(__file__)
load_file = current_file.parent / "student.json"

with open(load_file, "r") as file:
    data = json.load(file)
print(data)
print(type(data))