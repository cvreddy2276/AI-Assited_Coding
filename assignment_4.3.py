#give a python code for checking whether a given year is a leap year or not and takes input from user
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
#write a python code to convert the given input centimeters to meters and kilometers
cm = float(input("Enter length in centimeters: "))
meters = cm / 100
kilometers = cm / 100000
print(f"{cm} centimeters is equal to {meters} meters or {kilometers} kilometers.")
#write a python code to format the given full name in "Last Name, First Name" format
def format_name(full_name):
    name_parts = full_name.split()
    if len(name_parts) >= 2:
        first_name = name_parts[0]
        last_name = name_parts[-1]
        return f"{last_name}, {first_name}"
    else:
        return full_name
full_name = input("Enter full name: ")
print(format_name(full_name))
#Zero-Shot Version
#Generate a Python function that counts the number of vowels in a given string
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_string if char in vowels)
    return count
input_string = input("Enter a string: ")
print(f"Number of vowels: {count_vowels(input_string)}")

#Few-Shot Version
#Generate a Python function that counts vowels in a string
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in input_string if char in vowels)
    return count
input_string = input("Enter a string: ")
print(f"Number of vowels: {count_vowels(input_string)}")

#Generate a Python function that reads a .txt file, counts the number of lines in the file, and returns the line count.
def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        return 0

filename = input("Enter the name of the .txt file: ")
print(f"Number of lines in {filename}: {count_lines_in_file(filename)}")
