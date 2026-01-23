def is_leap_year(year: int) -> bool:
    """
    Determines if a given year is a leap year according to Gregorian calendar rules.

    A year is a leap year if it is divisible by 4, but not by 100 unless it is also divisible by 400.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
# Example usage:
'''year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")'''
def find_gcd(a: int, b: int) -> int:
    """
    Calculates the Greatest Common Divisor (GCD) of two integers using Euclid's algorithm.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The GCD of a and b.
    """
    while b != 0:
        a, b = b, a % b
    return a
# Example usage: 
'''num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
gcd = find_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {gcd}.")'''
def calculate_lcm(a: int, b: int) -> int:
    """
    Calculates the Least Common Multiple (LCM) of two integers.

    The LCM is the smallest positive integer that is a multiple of both a and b.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The LCM of a and b.
    """
    if a == 0 or b == 0:
        return 0  # LCM is undefined for zero, but per examples, assume positive integers
    gcd = find_gcd(a, b)
    return abs(a * b) // gcd
'''a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
lcm = calculate_lcm(a, b)
print(f"The LCM of {a} and {b} is {lcm}.")'''
def binary_to_decimal(binary: str) -> int:
    """
    Converts a binary string to its decimal integer equivalent.

    Args:
        binary (str): A string consisting of '0's and '1's representing a binary number.

    Returns:
        int: The decimal equivalent of the binary string.

    Raises:
        ValueError: If the string contains characters other than '0' and '1'.
    """
    if not all(c in '01' for c in binary):
        raise ValueError("Invalid binary string")
    return int(binary, 2)
def decimal_to_binary(decimal: int) -> str:
    """
    Converts a decimal integer to its binary string representation.

    Args:
        decimal (int): The decimal integer to convert.

    Returns:
        str: The binary representation as a string.
    """
    if decimal == 0:
        return "0"
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

# Example usage:
'''decimal_num = int(input("Enter a decimal number: "))
binary_rep = decimal_to_binary(decimal_num)
print(f"The binary representation of {decimal_num} is {binary_rep}.")'''
def check_harshad_number(num: int) -> bool:
    """
    Checks if a given integer is a Harshad (Niven) number.

    A Harshad number is an integer that is divisible by the sum of its digits.

    Args:
        num (int): The integer to check.

    Returns:
        bool: True if the number is a Harshad number, False otherwise.
    """
    if num <= 0:
        return False  # Harshad numbers are typically positive integers
    digit_sum = sum(int(digit) for digit in str(num))
    return num % digit_sum == 0

# Example usage:
num = int(input("Enter a number: "))
if check_harshad_number(num):
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")