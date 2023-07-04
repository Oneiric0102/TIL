import os
import glob

folder_path = "C:\\Users\\ndmjl\\Desktop\\Oreumi"

if not os.path.exists(folder_path):
    print(f"폴더 '{folder_path}는 존재하지 않습니다.")
else:
    print(f"폴더 '{folder_path}는 존재합니다.")

pdf_files = glob.glob('C:\\Users\\ndmjl\\Desktop\\*.pdf', recursive = True)

for pdf_file in pdf_files:
    print(pdf_file)

current_path = os.path.abspath(__file__)
print(current_path)