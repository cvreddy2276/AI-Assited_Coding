'''
Task 3 (Refactoring Repeated File Handling Code)
• Task: Use AI to refactor repeated file open/read/close logic.
• Focus Areas:
o DRY principle
o Context managers
o Function reuse
Legacy Code:
f = open("data1.txt")
print(f.read())
f.close()
f = open("data2.txt")
print(f.read())
f.close()
Expected Outcome:
o Reusable function using with open() and parameters.
'''
# Refactored version using a reusable function with context managers.
import os

def read_file(filename):
    with open(filename) as f:
        print(f.read())

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
read_file(os.path.join(script_dir, "data1.txt"))
read_file(os.path.join(script_dir, "data2.txt"))