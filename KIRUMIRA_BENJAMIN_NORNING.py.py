class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_new_salary(self, increment_amount):
        self.salary += increment_amount

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: {self.salary}")


# Creating an instance of the Employee class
employee = Employee("Kirumira Benjamin Edward", 850000)

# Displaying the initial employee information
print("Initial Employee Information:")
employee.display_info()

# Performing pay incrementation
increment_amount = 150000
employee.calculate_new_salary(increment_amount)

# Displaying the updated employee information
print("\nAfter Pay Incrementation:")
employee.display_info()
