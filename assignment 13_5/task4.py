'''
• Task: Refactor inefficient linear searches using appropriate
data structures.
• Focus Areas:
o Time complexity
o Data structure choice
Legacy Code:
users = ["admin", "guest", "editor", "viewer"]
name = input("Enter username: ")
found = False
for u in users:
if u == name:
found = True
print("Access Granted" if found else "Access Denied")
Expected Outcome:
o Use of sets or dictionaries with complexity justification.
'''
# Refactor inefficient linear searches using appropriate data structures.
users = {"admin", "guest", "editor", "viewer"}
name = input("Enter username: ")
if name in users:
    print("Access Granted")
else:
    print("Access Denied")