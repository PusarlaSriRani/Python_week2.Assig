class Employee:
    def __init__(self, employee_id, employee_name, salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.salary = salary

    def display(self):
        print("ID:", self.employee_id)
        print("Name:", self.employee_name)
        print("Salary:", self.salary)
        print()

emp1 = Employee(1, "Rahul", 30000)
emp2 = Employee(2, "Sneha", 35000)
emp3 = Employee(3, "Kiran", 40000)

emp1.display()
emp2.display()
emp3.display()