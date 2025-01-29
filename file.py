if __name__ == "__main__":
     from Employee import Employee
     emp = Employee("John Doe", 50000)
     print(f"Employee Name: {emp.get_name()}")
     print(f"Employee Salary: {emp.get_salary()}")
