from pathlib import Path

current_file = Path(__file__)

file_path = current_file.parent / "student.txt"

with open(file_path, "r") as file:
    content = file.readlines()
data = {}
for line in content:
    key, value = line.split(":")
    data[key.strip()] = value.strip()
print(data)