lines = ["Name: Imran",
         "Course: Computer Science",
         "Year: 3"]
data = {}
for line in lines:
    key, value = line.split(":")
    data[key.strip()] = value.strip()
print(data)