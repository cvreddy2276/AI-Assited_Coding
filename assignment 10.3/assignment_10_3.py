def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
print(factorial(5))

def perform_arithmetic_operation(first_number, second_number, operation):
    """
    Perform a basic arithmetic operation on two numbers.
    
    This function takes two numeric operands and an operation string,
    then returns the result of the specified arithmetic operation.
    Supports addition, subtraction, multiplication, and division.
    
    Parameters:
    -----------
    first_number : int or float
        The first operand for the arithmetic operation.
    second_number : int or float
        The second operand for the arithmetic operation.
    operation : str
        The arithmetic operation to perform. Must be one of:
        - "add": Addition (first_number + second_number)
        - "sub": Subtraction (first_number - second_number)
        - "mul": Multiplication (first_number * second_number)
        - "div": Division (first_number / second_number)
    
    Returns:
    --------
    int or float
        The result of the arithmetic operation.
    
    Raises:
    -------
    ValueError
        If operation is not one of the valid strings: "add", "sub", "mul", "div".
    ZeroDivisionError
        If operation is "div" and second_number is zero.
    TypeError
        If first_number or second_number are not numeric types.
    
    Examples:
    ---------
    >>> perform_arithmetic_operation(10, 5, "add")
    15
    >>> perform_arithmetic_operation(10, 5, "sub")
    5
    >>> perform_arithmetic_operation(10, 5, "mul")
    50
    >>> perform_arithmetic_operation(10, 5, "div")
    2.0
    
    >>> perform_arithmetic_operation(10, 0, "div")
    Traceback (most recent call last):
        ...
    ZeroDivisionError: Cannot divide by zero. Second operand must be non-zero.
    """
    
    # Input validation: Check types
    if not isinstance(first_number, (int, float)) or not isinstance(second_number, (int, float)):
        raise TypeError(
            f"Operands must be numeric (int or float). "
            f"Got: first_number={type(first_number).__name__}, "
            f"second_number={type(second_number).__name__}"
        )
    
    # Input validation: Check operation is valid
    valid_operations = {"add", "sub", "mul", "div"}
    if operation not in valid_operations:
        raise ValueError(
            f"Invalid operation '{operation}'. "
            f"Must be one of: {', '.join(sorted(valid_operations))}"
        )
    
    # Perform the operation
    if operation == "add":
        return first_number + second_number
    elif operation == "sub":
        return first_number - second_number
    elif operation == "mul":
        return first_number * second_number
    elif operation == "div":
        if second_number == 0:
            raise ZeroDivisionError(
                "Cannot divide by zero. Second operand must be non-zero."
            )
        return first_number / second_number

def check_Prime(number: int) -> bool:
    """
    Determine whether an integer is prime.

    Parameters
    ----------
    number : int
        The integer to test for primality.

    Returns
    -------
    bool
        `True` if `number` is prime, otherwise `False`.

    Raises
    ------
    TypeError
        If `number` is not an `int`.

    Examples
    --------
    >>> check_Prime(2)
    True
    >>> check_Prime(15)
    False
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an int")

    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    limit = int(number ** 0.5) + 1
    for i in range(3, limit, 2):
        if number % i == 0:
            return False
    return True


def sum_of_squares(numbers):
    """Compute the sum of squares using a simple loop."""
    total = 0
    for num in numbers:
        total += num ** 2
    return total


def sum_of_squares_optimized(numbers):
    """Compute the sum of squares using Python's built-in sum and a generator."""
    return sum(x * x for x in numbers)


if __name__ == "__main__":
    import time

    size = 1_000_000
    values = range(size)

    t0 = time.perf_counter()
    result1 = sum_of_squares(values)
    elapsed1 = time.perf_counter() - t0

    t0 = time.perf_counter()
    result2 = sum_of_squares_optimized(values)
    elapsed2 = time.perf_counter() - t0

    print(f"sum_of_squares result: {result1}, elapsed: {elapsed1:.4f}s")
    print(f"sum_of_squares_optimized result: {result2}, elapsed: {elapsed2:.4f}s")

