"""
Logical operators are used to perform logical operations:
AND, OR, and NOT.

They are commonly used to combine multiple conditional statements.
"""

# Example One (with boolean values)

a = False
b = True

print("a AND b:", a and b)    # False AND True → False
print("a OR b:", a or b)      # False OR True → True
print("NOT b:", not b)        # NOT True → False

# Example Two (with conditions)

a = 10
b = 20

print("a > b and b > a:", a > b and b > a)   # False and True → False
print("a > b or a < b:", a > b or a < b)     # False or True → True
print("not (a > b or a < b):", not (a > b or a < b)) # not(True) → False
