# Base class representing a generic Employee
class Employee:
    def __init__(self, first_name, last_name, salary, gender, department, car_driven):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.gender = gender
        self.department = department
        self.car_driven = car_driven

    def display_info(self):
        # Displaying common employee information
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Salary: ${self.salary}")
        print(f"Gender: {self.gender}")
        print(f"Department: {self.department}")
        print(f"Car Driven: {self.car_driven}")
        print()


# Manager class, derived from Employee
class Manager(Employee):
    def __init__(self, first_name, last_name, salary, gender, department, car_driven, team_size):
        # Calling the constructor of the base class
        super().__init__(first_name, last_name, salary, gender, department, car_driven)
        self.team_size = team_size

    def display_info(self):
        # Displaying manager-specific information
        super().display_info()
        print(f"Team Size: {self.team_size}")
        print("Manager Details:")
        print("Responsible for managing a team.")
        print()


# Engineer class, derived from Employee
class Engineer(Employee):
    def __init__(self, first_name, last_name, salary, gender, department, car_driven, programming_language):
        # Calling the constructor of the base class
        super().__init__(first_name, last_name, salary, gender, department, car_driven)
        self.programming_language = programming_language

    def display_info(self):
        # Displaying engineer-specific information
        super().display_info()
        print(f"Programming Language: {self.programming_language}")
        print("Engineer Details:")
        print("Works on software development projects.")
        print()


# SeniorEngineer class, derived from Engineer
class SeniorEngineer(Engineer):
    def __init__(self, first_name, last_name, salary, gender, department, car_driven, programming_language, years_of_experience):
        # Calling the constructor of the base class
        super().__init__(first_name, last_name, salary, gender, department, car_driven, programming_language)
        self.years_of_experience = years_of_experience

    def display_info(self):
        # Displaying senior engineer-specific information
        super().display_info()
        print(f"Years of Experience: {self.years_of_experience}")
        print("Senior Engineer Details:")
        print("Senior engineers have extensive experience in software development.")
        print()


# Example Usage
employee_data = [
    {"first_name": "John", "last_name": "Doe", "salary": 6000, "gender": "Male", "department": "HR", "car_driven": "Toyota"},
    {"first_name": "Alice", "last_name": "Smith", "salary": 8000, "gender": "Female", "department": "Engineering", "car_driven": "Honda", "programming_language": "Python"},
    {"first_name": "Bob", "last_name": "Johnson", "salary": 7000, "gender": "Male", "department": "Management", "car_driven": "Ford", "team_size": 10},
    {"first_name": "Eva", "last_name": "Brown", "salary": 9000, "gender": "Female", "department": "Engineering", "car_driven": "Tesla", "programming_language": "Java", "years_of_experience": 8}
]

employees = []

for data in employee_data:
    if "years_of_experience" in data:
        employee = SeniorEngineer(**data)
    elif "programming_language" in data:
        employee = Engineer(**data)
    elif "team_size" in data:
        employee = Manager(**data)
    else:
        employee = Employee(**data)
    employees.append(employee)

# Displaying information
for employee in employees:
    employee.display_info()
