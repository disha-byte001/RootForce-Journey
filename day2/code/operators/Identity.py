"""
Identity operators are used to check if two variables refer to the exact same object in memory.

- 'is'      → Returns True if both variables point to the same object
- 'is not'  → Returns True if they point to different objects
"""

# First example — using funny names to understand the concept 😄

ram = [1, 2, 3]
shyam = [1, 2, 3]
rahul = ram  # Ram and Rahul are the same person with a different name (same object)

print("ram is shyam:", ram is shyam)     # False → different objects (even if values match)
print("ram is rahul:", ram is rahul)     # True → same object, just a different name


# Second example — using a real coding case

a = [10, 20, 40]
b = [10, 30, 40]
c = a  # c points to the same object as a

print("a is not b:", a is not b)   # True → different objects (even if similar-looking)
print("a is b:", a is b)           # False → different memory locations
print("a is not c:", a is not c)   # False → c is the same object as a
print("a is c:", a is c)           # True → exact same object

# 💡 Think of it like this:
# a and c are twins using the same phone 📱
# But a and b are strangers who bought the same model — not the same device!
