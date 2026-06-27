d = {
    "a": 1,
    "b": 2
}

copy_dict = d.copy()

d.setdefault("c", 3)

d.setdefault("a", 100)

print("Original Dictionary:", d)
print("Copied Dictionary:", copy_dict)