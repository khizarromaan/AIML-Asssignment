class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def display(self):
        print(f"Car Brand: {self.brand} , Model: {self.model}")
        
car1 = car("Mercedes","AMG G 63")
car2 = car("Rolls Royce", "Phantom")

car1.display()
car2.display()
        