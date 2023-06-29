file_path = "D:\\project\\TIL\\Oreumi\\Python\\file_1.txt"

with open(file_path, 'r') as file:
 content = file.read().split("\n")

content.sort()
print(content)
total_num = len(content)
print(total_num)
set_content=set(content)
print(set_content)