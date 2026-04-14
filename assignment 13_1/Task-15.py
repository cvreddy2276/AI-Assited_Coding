'''Task 15 (Vowel & Consonant Counter – Test Case Design)
• Function: Count vowels and consonants in string.
• Test Cases to Design:
•	Normal: "hello" → (2,3)
•	Edge: "" → (0,0)
•	Only vowels: "aeiou" → (5,0)
Large: Long text
• Requirement: Validate correctness with pytest.
'''

def count_vowels_consonants(s):
    """
    Count the number of vowels and consonants in a given string.

    Parameters:
    s (str): The input string to analyze.

    Returns:
    tuple: A tuple containing the count of vowels and consonants in the format (vowels, consonants).
    """
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0
    
    for char in s:
        if char.isalpha():  # Check if the character is an alphabet
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count
# Example usage
input_string = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(input_string)
print("Vowels:", vowels)
print("Consonants:", consonants)
