from pathlib import Path
import os

if __name__ == "__main__":
    file_path = Path(__file__).with_name("student.txt")

    if not file_path.exists():
        raise FileNotFoundError(f"Could not find {file_path}")

    with file_path.open("r", encoding="utf-8") as file:
        content = file.read()

    print(content.strip())

print(os.getcwd())



print("Current Working Directory:")
print(os.getcwd())

with open("week-01/student.txt", "r") as file:
    content = file.read()

print("\nStudent Data:")
print(content)

current_file = Path(__file__)

file_path = current_file.parent / "student.txt"

with open(file_path, "r") as file:
    content = file.read()

print(content.strip())