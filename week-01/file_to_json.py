from pathlib import Path
import json

current_file = Path(__file__)

input_file = current_file.parent / "student.txt"

with open(input_file, "r") as file:
    content = file.readlines()
data = {}
for line in content:
    key, value = line.split(":")
    data[key.strip()] = value.strip()

output_file = current_file.parent / "student.json"
copy_file = current_file.parent / "student_copy.json"

with open(output_file, "w") as file:
    json.dump(data, file, indent = 4)

with open(copy_file, "w") as file:
    json.dump(data, file, indent = 4)

print("Data successfully written to student.json")
print(data)