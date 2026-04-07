'''
• Task: Use AI to refactor a performance-heavy loop handling
large data.
• Focus Areas:
o Algorithmic optimization
o Use of built-in functions
Legacy Code:
total = 0
for i in range(1, 1000000):
if i % 2 == 0:
total += i
print(total)
Expected Outcome:
o Optimized logic using mathematical formulas or
comprehensions, with time comparison.
'''
# Refactor performance-heavy loop handling large data by using in buit functions and mathematical formulas.
total = sum(i for i in range(1, 1000000) if i % 2 == 0)
print(total)
