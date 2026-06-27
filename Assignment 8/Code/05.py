s = {100, 200, 300, 400, 500}

removed = s.pop()
print("Removed:", removed)

print("After pop:", s)

s.clear()

print("After clear:", s)

# remove() removes given element.
# discard() removes an element without error if it doesn't exist.
# pop() removes last element from the set.