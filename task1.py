# Accepting user input
user_input = input("Enter a string to reverse: ")

# Initializing an empty string to store the result
reversed_string = ""

#Logic to reverse the string using a loop
for i in range(len(user_input)-1,-1,-1):
    reversed_string += user_input[i]

#Printing the result
print("Original String:", user_input)
print("Reversed String:", reversed_string)
