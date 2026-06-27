class Person:
    def __init__(self, name, age): 
        self.name = name 
        self.age = age
        
    def introduce(self):
        print("My name is", self.name, "and I am", self.age, "years old.")

p1 = Person("Khizar", 18)
p1.introduce()