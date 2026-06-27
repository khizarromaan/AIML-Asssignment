import mymodule as mm

name = input("Enter Your Name: ")

mm.greet(name)

base = int(input("Enter Base: "))
exp = int(input("Enter Exponent: "))

result = mm.calculate_power(base, exp)

print("Power =", result)