from pathlib import Path
import json

def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.readlines()
    return [line.strip() for line in content]

def parse_data(lines):
    data = {}
    for line in lines:
         try:
                key, value = line.split(":",1)
                data[key.strip()] = value.strip()

         except ValueError:
                print(f"Skipping invalid line: {line}")
    return data

def save_json(data, output_file):
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Data successfully written to {output_file.name}")

current_file = Path(__file__)
input_file = current_file.parent / "student.txt"
output_file = current_file.parent / "student.json"

lines = read_file(input_file)

data = parse_data(lines)

save_json(data, output_file)