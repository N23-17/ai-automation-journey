lines = ["Name: Imran",
         "Course Computer Science",
         "Year: 3"]
data = {}
for line in lines:
    try:
        key, value = line.split(":")
        data[key.strip()] = value.strip()

    except ValueError:
        print(f"Skipping invalid line: {line}")
print(data)