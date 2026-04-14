'''Task Description #1 (Refactoring – Removing Code Duplication)
•	Task: Use AI to refactor a given Python script that contains multiple repeated code blocks.
•	Instructions:
o	Prompt AI to identify duplicate logic and replace it with functions or classes.
o	Ensure the refactored code maintains the same output.
o	Add docstrings to all functions.
•	Sample Legacy Code:
# Legacy script with repeated logic
print("Area of Rectangle:", 5 * 10)
print("Perimeter of Rectangle:", 2 * (5 + 10))

print("Area of Rectangle:", 7 * 12)
print("Perimeter of Rectangle:", 2 * (7 + 12))

print("Area of Rectangle:", 10 * 15)
print("Perimeter of Rectangle:", 2 * (10 + 15))
•	Expected Output:
o	Refactored code with a reusable function and no duplication.
o	Well documented code
'''

# Refactored script with functions to remove code duplication
def calculate_rectangle_properties(length, width):
    """
    Calculate the area and perimeter of a rectangle.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    tuple: A tuple containing the area and perimeter of the rectangle.
    """
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
# List of rectangles with their dimensions
rectangles = [(5, 10), (7, 12), (10, 15)]
# Calculate and print the properties of each rectangle
for length, width in rectangles:
    area, perimeter = calculate_rectangle_properties(length, width)
    print(f"Area of Rectangle: {area}")
    print(f"Perimeter of Rectangle: {perimeter}")

