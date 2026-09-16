my_list = [1, 2.5, 3, 4.2]

# Returns True only if every item is strictly an int or a float
result = all(type(item) in (int, float) for item in my_list)
print(result)  # Output: True

# This will correctly return False if a boolean is present:
bad_list = [1, 2.5, True]
print(all(type(item) in (int, float) for item in bad_list))  # Output: False