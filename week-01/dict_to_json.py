from pathlib import Path
import json

current_file = Path(__file__)
output_file = current_file.parent / "student.json"

student = {'Name': 'Utulele',
 'Course': 'Computer Science',
 'Year': '3'}
with open(output_file, "w") as file:
    json.dump(student, file, indent = 2)

print("successfully done")