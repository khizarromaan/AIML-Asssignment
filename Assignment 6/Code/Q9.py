# Create two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("list1:",list1)
print("list2:",list2)
list_extend = list1.copy()

list_extend.extend(list2)
print("Using extend():", list_extend)

list_append = list1.copy()

list_append.append(list2)
print("Using append():", list_append)
