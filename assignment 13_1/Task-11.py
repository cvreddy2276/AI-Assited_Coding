'''		Task 11 – Refactoring the Harshad (Niven) Number Checker
Refactor the given poorly structured Python script into a clean, modular, and reusable implementation.
A Harshad (Niven) number is a number that is divisible by the sum of its digits.
For example:
•	18 → 1 + 8 = 9 → 18 ÷ 9 = 2 ✅ (Harshad Number)
•	19 → 1 + 9 = 10 → 19 ÷ 10 ≠ integer ❌ (Not Harshad)

Problem Statement
The current implementation:
•	Mixes logic and input handling
•	Uses redundant variables
•	Does not use reusable functions properly
•	Returns print statements instead of boolean values
•	Lacks documentation
You must refactor the code to follow clean coding principles.
# Harshad Number Checker (Unstructured Version)

num = int(input("Enter a number: "))

temp = num
sum_digits = 0

while temp > 0:
    digit = temp % 10
    sum_digits = sum_digits + digit
    temp = temp // 10

if sum_digits != 0:
    if num % sum_digits == 0:
        print("True")
    else:
        print("False")
else:
    print("False")
You must:
1.	Create a reusable function: is_harshad(number)
2.	The function must:
o	Accept an integer parameter.
o	Return True if the number is divisible by the sum of its digits.
o	Return False otherwise.
3.	Separate user input from core logic.
4.	Add proper docstrings.
5.	Improve readability and maintainability.
6.	Ensure the program handles edge cases (e.g., 0, negative numbers).
		
'''

def is_harshad(number):
    """
    Check if a number is a Harshad (Niven) number.

    Parameters:
    number (int): The number to check.

    Returns:
    bool: True if the number is a Harshad number, False otherwise.
    """
    if number < 0:
        return False  # Harshad numbers are typically defined for non-negative integers

    sum_digits = sum(int(digit) for digit in str(number))

    if sum_digits == 0:
        return False  # Avoid division by zero

    return number % sum_digits == 0
# Get user input
user_input = int(input("Enter a number: "))
# Check if the number is a Harshad number and print the result
if is_harshad(user_input):
    print("True")
else:    print("False")

