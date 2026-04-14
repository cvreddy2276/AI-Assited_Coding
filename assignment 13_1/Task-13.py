'''		Test Cases Design
Task 13 (Collatz Sequence Generator – Test Case Design)
• Function: Generate Collatz sequence until reaching 1.
• Test Cases to Design:
•	Normal: 6 → [6,3,10,5,16,8,4,2,1]
•	Edge: 1 → [1]
•	Negative: -5
•	Large: 27 (well-known long sequence)
• Requirement: Validate correctness with pytest.
Explanation: 
We need to write a function that:
•	Takes an integer n as input.
•	Generates the Collatz sequence (also called the 3n+1 sequence).
•	The rules are:
o	If n is even → next = n / 2.
o	If n is odd → next = 3n + 1.
•	Repeat until we reach 1.
•	Return the full sequence as a list.


Example 
Input: 6
Steps:
•	6 (even → 6/2 = 3)
•	3 (odd → 3*3+1 = 10)
•	10 (even → 10/2 = 5)
•	5 (odd → 3*5+1 = 16)
•	16 (even → 16/2 = 8)
•	8 (even → 8/2 = 4)
•	4 (even → 4/2 = 2)
•	2 (even → 2/2 = 1)
Output:
[6, 3, 10, 5, 16, 8, 4, 2, 1]		
'''

def collatz_sequence(n):
    """
    Generate the Collatz sequence for a given integer n until reaching 1.

    Parameters:
    n (int): The starting integer for the Collatz sequence.

    Returns:
    list: A list containing the Collatz sequence from n to 1.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    sequence = []
    
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    
    sequence.append(1)  # Append the final element of the sequence
    return sequence
# Example usage
try:
    n = int(input("Enter a positive integer: "))
    print(collatz_sequence(n))
except ValueError as e:
    print(e)

    