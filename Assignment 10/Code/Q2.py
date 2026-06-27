class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
    def show_details(self):
        print("Title:", self.title, "Author:", self.author, "Price: INR", self.price)

book1 = Book("Harry Potter and the chambers of secret", "J.K. Rowling", 499)
book2 = Book("The Chronicles of Narnia", "C.S. Lewis", 399)

book1.show_details()
book2.show_details()