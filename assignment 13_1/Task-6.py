'''Task 6 (Optimizing Search Logic)
• Task: Refactor inefficient linear searches using appropriate data structures.
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
o Use of sets or dictionaries with complexity justification
'''

def check_user_access(username, user_set):
    """
    Check if the given username exists in the user set.

    Parameters:
    username (str): The username to check.
    user_set (set): A set of valid usernames.

    Returns:
    bool: True if access is granted, False otherwise.
    """
    return username in user_set
# Create a set of users for O(1) average time complexity lookups
users = {"admin", "guest", "editor", "viewer"}
# Get the username input from the user
name = input("Enter username: ")
# Check access and print the result
if check_user_access(name, users):
    print("Access Granted")
else:    print("Access Denied")
