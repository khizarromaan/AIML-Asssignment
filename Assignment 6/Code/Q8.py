marks = [45, 78, 65, 90, 34, 82, 71]
original = marks.copy()
print("original list:",marks)
marks.sort()
print("Ascending order:",marks)
marks.sort(reverse=True)
print("descending order:",marks)
original.reverse()
print("Reverse of original list:",original)