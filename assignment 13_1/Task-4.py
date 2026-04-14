'''Task Description #4 (Refactoring – Converting Procedural Code to Functions)
• Task: Use AI to refactor procedural input–processing logic into functions.
Instructions:
o Identify input, processing, and output sections.
o Convert each into a separate function.
o Improve code readability without changing behavior.
• Sample Legacy Code:
num = int(input("Enter number: "))
square = num * num
print("Square:", square)
• Expected Output:
o Modular code using functions like get_input(), calculate_square(), and display_result().
'''

def get_input():
    """
    Prompt the user to enter a number and return it.

    Returns:
    int: The number entered by the user.
    """
    num = int(input("Enter number: "))
    return num
def calculate_square(num):
    """Calculate the square of a given number.
    Parameters:
    num (int): The number to be squared.
    Returns:
    int: The square of the given number.
    """
    return num * num
def display_result(square):
    """
    Display the calculated square.

    Parameters:
    square (int): The square to be displayed.
    """
    print("Square:", square)
# Main execution flow
num = get_input()
square = calculate_square(num)
display_result(square)
