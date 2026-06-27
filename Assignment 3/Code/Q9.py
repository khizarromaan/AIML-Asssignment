total = 0

def add_value(x):
    global total
    total = total + x

    local_var = x
    print("Local Variable:", local_var)

add_value(10)
print("Total =", total)

add_value(10)
print("Total =", total)

add_value(20)
# print("local variable =", local_var)