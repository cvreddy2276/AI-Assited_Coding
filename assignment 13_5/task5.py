'''
• Task: Use AI to refactor procedural code into a class-based
design.
• Focus Areas:
o Object-Oriented principles
o Encapsulation
Legacy Code:
salary = 50000
tax = salary * 0.2
net = salary - tax
print(net)
Expected Outcome:
o A class like EmployeeSalaryCalculator with methods and
attributes.
'''
#refactor procedural code into a class-based design.
class EmployeeSalaryCalculator:
    def __init__(self, salary):
        self.salary = salary
        self.tax_rate = 0.2

    def calculate_tax(self):
        return self.salary * self.tax_rate

    def calculate_net_salary(self):
        tax = self.calculate_tax()
        return self.salary - tax

# Example usage
calculator = EmployeeSalaryCalculator(50000)
print(calculator.calculate_net_salary())