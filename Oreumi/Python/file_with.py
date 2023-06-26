file_path = "example.txt"

with open(file_path, 'r') as file:
 content = file.read()
 print(content)

file_path = "example.txt"
content = "Hello, World!"
with open(file_path, 'w') as file:
 file.write(content)