students = {
    "Anil": {"Marks": 90, "Grade": "A"},
    "Priya": {"Marks": 95, "Grade": "A+"},
    "Rahul": {"Marks": 80, "Grade": "B"},
    "Sneha": {"Marks": 88, "Grade": "A"},
    "Kiran": {"Marks": 76, "Grade": "B"}
}

for name, details in students.items():
    print(name, details)

highest = max(students, key=lambda x: students[x]["Marks"])

print("Highest Marks Student:", highest)