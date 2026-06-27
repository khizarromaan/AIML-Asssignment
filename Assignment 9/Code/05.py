info = {"brand": "Samsung", "model": "A52", "price": 25000}

print("Original Dictionary:",info)

info.update({"color": "Black", "price": 24000})

print("Updated Dictionary:",info)

print("Popped item:",info.pop("model"))

print("final dictionary:", info)