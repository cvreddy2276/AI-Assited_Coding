'''		Task 12 – Refactoring the Factorial Trailing Zeros Program
Refactor the given poorly structured Python script into a clean, modular, and efficient implementation.
The program calculates the number of trailing zeros in n! (factorial of n).
Problem Statement
The current implementation:
•	Calculates the full factorial (inefficient for large n)
•	Mixes input handling with business logic
•	Uses print statements instead of return values
•	Lacks modular structure and documentation
You must refactor the code to improve efficiency, readability, and maintainability.





# Factorial Trailing Zeros (Unstructured Version)
n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact = fact * i
    i = i + 1
count = 0
while fact % 10 == 0:
    count = count + 1
    fact = fact // 10
print("Trailing zeros:", count)
You must:
1.	Create a reusable function: count_trailing_zeros(n)
2.	The function must:
o	Accept a non-negative integer n.
o	Return the number of trailing zeros in n!.
3.	Do NOT compute the full factorial.
4.	Use an optimized mathematical approach (count multiples of 5).
5.	Add proper docstrings.
6.	Separate user interaction from core logic.
7.	Handle edge cases (e.g., negative numbers, zero).		
'''

def count_trailing_zeros(n):
    """
    Count the number of trailing zeros in n! (factorial of n).

    Parameters:
    n (int): A non-negative integer for which to count trailing zeros in its factorial.

    Returns:
    int: The number of trailing zeros in n!.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    count = 0
    power_of_5 = 5
    
    while n >= power_of_5:
        count += n // power_of_5
        power_of_5 *= 5
    
    return count
# Example usage
try:
    n = int(input("Enter a non-negative integer: "))
    print("Trailing zeros in {}!: {}".format(n, count_trailing_zeros(n)))
except ValueError as e:
    print(e)
