name = "Glass"
quantity = 500
price = 100.99
is_available = True

print("Product",name, type(name))
print("Quantity",quantity, type(quantity))
print("Price",price,type(price))
print("Availability",is_available, type(is_available))

# Type conversion
floatQuantity = float(quantity)
intPrice = int(price)

print("Int converted into Float: " , floatQuantity)
print("Float converted into Int: " , intPrice)