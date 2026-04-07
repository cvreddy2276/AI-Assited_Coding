'''
Task Description #2 : (Refactoring Deeply Nested Conditionals)
• Task: Use AI to refactor deeply nested if–elif–else logic into a
cleaner structure.
• Focus Areas:
o Readability
o Logical simplification
o Maintainability
Legacy Code:
score = 78
if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Very Good")
elif score >= 60:
    print("Good")
else:
    print("Needs Improvement")
Expected Outcome:
o Flattened logic using guard clauses or a mapping-based
approach.
'''
# Refactored version Flattened logic using guard clauses or a mapping-based approach.
score = 78
if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Very Good")
elif score >= 60:
    print("Good")
else:
    print("Needs Improvement")