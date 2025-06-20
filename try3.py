import os

current_path = os.getcwd()
print(current_path)  # Текущий рабочий каталог


relative_path = 'folder/subfolder/file.txt'
absolute_path = os.path.abspath(relative_path)
print(absolute_path)  # Полный путь к файлу


path = 'folder/subfolder/file.txt'
if os.path.exists(path):
    print("Путь существует")
else:
    print("Путь не существует")

# Создание пути с использованием os.path.join
path = os.path.join('folder', 'subfolder', 'file.txt')
print(path)  # Вывод: folder/subfolder/file.txt (на Unix) или folder\subfolder\file.txt (на Windows)
