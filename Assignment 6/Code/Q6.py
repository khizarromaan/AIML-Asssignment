items = [10, 20, 30, 20, 40, 50]
print("original list",items)
items.remove(20)
print("removed first 20",items)
print("Removed item:",items.pop(3))
print("removed 40 from 3rd index",items)
items.pop(-1)
print("removed last item",items)
items.clear()
print("after clearing the list",items)


