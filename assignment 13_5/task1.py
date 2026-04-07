'''Task Description #1 (Refactoring – Removing Global Variables)
• Task: Use AI to eliminate unnecessary global variables from the
code.
• Instructions:
o Identify global variables used across functions.
o Refactor the code to pass values using function parameters.
o Improve modularity and testability.
• Sample Legacy Code:
rate = 0.1
def calculate_interest(amount):
return amount * rate
print(calculate_interest(1000))
• Expected Output:
o Refactored version passing rate as a parameter or using a
configuration structure.'''

# Refactored version passing rate as a parameter or using a configuration structure.
def calculate_interest(amount, rate):
    return amount * rate
print(calculate_interest(1000, 0.1))