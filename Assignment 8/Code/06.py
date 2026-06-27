set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}

copyset = set1.copy()

set1.update(set2)

print("Original Copy:", copyset)
print("Updated Set:", set1)