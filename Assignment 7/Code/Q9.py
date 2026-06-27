coordinates = (10, 20)
print("original tuple:",coordinates)
# Tuples are immutable

# coordinates[0] = 100
# Error:
# TypeError: 'tuple' object does not support item assignment

# coordinates.append(30)
# Error:
# AttributeError: 'tuple' object has no attribute 'append'

# Correct way

list = list(coordinates)

list[0] = 100
list.append(30)

coordinates = tuple(list)

print("Modified Tuple:", coordinates)