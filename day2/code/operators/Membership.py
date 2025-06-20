"""
Membership operators are used to check if a value exists within a sequence (like list, string, tuple).

- 'in'     → Returns True if the value is present
- 'not in' → Returns True if the value is NOT present
"""

# Meet Ram and his backpack of tools
ram_tools = ["laptop", "notebook", "pen", "hacking_book"]

# Let's test what's inside Ram's bag
print("Is 'pen' in Ram's bag?", "pen" in ram_tools)            # True
print("Is 'flute' not in Ram's bag?", "flute" not in ram_tools)  # True
print("Is 'hacking_book' in Ram's bag?", "hacking_book" in ram_tools)  # True
print("Is 'phone' in Ram's bag?", "phone" in ram_tools)        # False
