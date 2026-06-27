fruits = ('apple', 'banana', 'cherry', 'banana', 'mango', 'apple')

print("First index of banana:",fruits.index("banana"))
print("First index of banana starting from index 2:",fruits.index("banana",2))
try:
    print("index of kiwi:",fruits.index('kiwi'))
except:
      print("Not Found")