'''Task 9 – Twin Primes Checker
Twin primes are pairs of primes that differ by 2 (e.g., 11 and 13, 17 and 19).
The initial code has:
•	Inefficient prime checking.
•	No functions.
•	Hardcoded inputs.
Task for Students:
•	Refactor into is_prime(n) and is_twin_prime(p1, p2).
•	Add docstrings and optimize.
•	Generate a list of twin primes in a given range using AI.
Bad Code Version:
# twin primes bad version
a=11
b=13
fa=0
for i in range(2,a):
 if a%i==0:
  fa=1
fb=0
for i in range(2,b):
 if b%i==0:
  fb=1
if fa==0 and fb==0 and abs(a-b)==2:
 print("Twin Primes")
else:
 print("Not Twin Primes")
'''

def is_prime(n):
    """
    Check if a number is prime.
    Parameters:
    n (int): The number to check for primality.
    Returns:
    bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_twin_prime(p1, p2):
    """Check if two numbers are twin primes."""
    if is_prime(p1) and is_prime(p2) and abs(p1 - p2) == 2:
        return True
    return False
def generate_twin_primes(limit):
    """Generate a list of twin primes up to a given limit.
    Parameters:
    limit (int): The upper limit for generating twin primes.
    Returns:
    list: A list of tuples, each containing a pair of twin primes.
    """
    twin_primes = []
    for num in range(2, limit):
        if is_twin_prime(num, num + 2):
            twin_primes.append((num, num + 2))
    return twin_primes
# Get the limit input from the user
limit = int(input("Enter the upper limit for twin primes: "))
# Generate and print the list of twin primes
twin_prime_list = generate_twin_primes(limit)
print("Twin Primes up to", limit, ":", twin_prime_list)
