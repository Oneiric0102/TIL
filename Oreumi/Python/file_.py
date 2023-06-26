file_path = "example.txt"
file = open(file_path, 'r', encoding="utf-8")

content = file.read()
print(content)

file.close()

file_path = "example.txt"
file = open(file_path, 'w')

file.write("test context.")

file.close()