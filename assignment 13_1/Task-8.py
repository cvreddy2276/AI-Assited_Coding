'''		Task 8– Fibonacci Generator
Write a program to generate Fibonacci series up to n.
The initial code has:
•	Global variables.
•	Inefficient loop.
•	No functions or modularity.
Task for Students:
•	Refactor into a clean reusable function (generate_fibonacci).
•	Add docstrings and test cases.
•	Compare AI-refactored vs original.
Bad Code Version:
# fibonacci bad version
n=int(input("Enter limit: "))
a=0
b=1
print(a)
print(b)
for i in range(2,n):
 c=a+b
 print(c)
 a=b
 b=c		
'''

def generate_fibonacci(n):
    """
    Generate Fibonacci series up to n.

    Parameters:
    n (int): The number of Fibonacci numbers to generate.

    Returns:
    list: A list containing the Fibonacci series up to n.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_series = [0, 1]
    for i in range(2, n):
        c = fib_series[i - 1] + fib_series[i - 2]
        fib_series.append(c)
    
    return fib_series
# Test cases
x = int(input("Enter limit: "))
print(generate_fibonacci(x)) 