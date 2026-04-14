'''Task Description #2 (Refactoring – Extracting Reusable Functions)
•	Task: Use AI to refactor a legacy script where multiple calculations are embedded directly inside the main code block.
•	Instructions:
o	Identify repeated or related logic and extract it into reusable functions.
o	Ensure the refactored code is modular, easy to read, and documented with docstrings.
•	Sample Legacy Code:


# Legacy script with inline repeated logic
price = 250
tax = price * 0.18
total = price + tax
print("Total Price:", total)

price = 500
tax = price * 0.18
total = price + tax
print("Total Price:", total)

•	Expected Output:
o	Code with a function calculate_total(price) that can be reused for multiple price inputs.
o	Well documented code
'''

def calculate_total(price):
    """
    Calculate the total price including tax.

    Parameters:
    price (float): The base price of the item.

    Returns:
    float: The total price including tax.
    """
    tax = price * 0.18
    total = price + tax
    return total

# Using the function for multiple prices
prices = [250, 500]
for price in prices:
    total = calculate_total(price)
    print("Total Price:", total)
