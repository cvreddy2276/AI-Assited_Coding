'''		Task 14 (Lucas Number Sequence – Test Case Design)
• Function: Generate Lucas sequence up to n terms.
(Starts with 2,1, then Fn = Fn-1 + Fn-2)
• Test Cases to Design:
•	Normal: 5 → [2, 1, 3, 4, 7]
•	Edge: 1 → [2]
•	Negative: -5 → Error
•	Large: 10 (last element = 76).
• Requirement: Validate correctness with pytest.
		
'''

def lucas_sequence(n):
    """
    Generate the Lucas sequence up to n terms.

    Parameters:
    n (int): The number of terms in the Lucas sequence to generate.

    Returns:
    list: A list containing the first n terms of the Lucas sequence.
    """
    if n < 1:
        raise ValueError("Input must be a positive integer.")
    
    sequence = []
    
    for i in range(n):
        if i == 0:
            sequence.append(2)
        elif i == 1:
            sequence.append(1)
        else:
            next_value = sequence[i-1] + sequence[i-2]
            sequence.append(next_value)
    
    return sequence
# Example usage
try:
    n = int(input("Enter the number of terms for the Lucas sequence: "))
    print(lucas_sequence(n))
except ValueError as e:
    print(e)
    