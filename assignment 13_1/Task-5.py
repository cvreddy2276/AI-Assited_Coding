'''Task 5 (Refactoring Procedural Code into OOP Design)
• Task: Use AI to refactor procedural code into a class-based design.
Focus Areas:
o Object-Oriented principles
o Encapsulation
Legacy Code:
salary = 50000
tax = salary * 0.2
net = salary - tax
print(net)
Expected Outcome:
o A class like EmployeeSalaryCalculator with methods and attributes.
'''

class EmployeeSalaryCalculator:
    """
    A class to calculate the net salary of an employee after tax deduction.
    """

    def __init__(self, salary):
        """
        Initialize the EmployeeSalaryCalculator with the given salary.

        Parameters:
        salary (float): The gross salary of the employee.
        """
        self.salary = salary

    def calculate_net_salary(self):
        """
        Calculate the net salary after deducting tax.

        Returns:
        float: The net salary after tax deduction.
        """
        tax = self.salary * 0.2
        net_salary = self.salary - tax
        return net_salary
# Create an object of the EmployeeSalaryCalculator class
employee = EmployeeSalaryCalculator(int(input("Enter the gross salary: ")))
# Call the method to calculate net salary and print the result
net_salary = employee.calculate_net_salary()
print(net_salary)
