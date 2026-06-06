file = open("students.txt", "w")

file.write("Anil\n")
file.write("Priya\n")
file.write("Rahul\n")
file.write("Sneha\n")
file.write("Kiran\n")

file.close()

file = open("students.txt", "r")

content = file.read()

print(content)

names = content.split("\n")

print("Total Students:", len(names) - 1)

file.close()