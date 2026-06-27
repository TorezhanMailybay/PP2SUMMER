import os

with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Line 1: Hello, World!\n")
    f.write("Line 2: Python File Handling\n")
    f.write("Line 3: Writing to files is easy!\n")

print("File 'sample.txt' created and written.")

students = [
    "Alice, 20, CS\n",
    "Bob, 22, Math\n",
    "Carol, 21, Physics\n",
    "Dave, 23, Biology\n",
]

with open("students.txt", "w", encoding="utf-8") as f:
    f.writelines(students)

print("File 'students.txt' created with writelines().")

with open("sample.txt", "a", encoding="utf-8") as f:
    f.write("Line 4: Appended line!\n")
    f.write("Line 5: One more appended line!\n")

print("Appended 2 lines to 'sample.txt'.")

exclusive_file = "exclusive.txt"
if os.path.exists(exclusive_file):
    os.remove(exclusive_file)

with open(exclusive_file, "x", encoding="utf-8") as f:
    f.write("This file was created exclusively with mode 'x'.\n")

print("File 'exclusive.txt' created with mode 'x'.")

print("\n--- Contents of sample.txt ---")
with open("sample.txt", "r", encoding="utf-8") as f:
    print(f.read())
