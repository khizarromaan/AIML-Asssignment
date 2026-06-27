class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.status = "Available"
        
    def issue_book(self):
        if self.status == "Available":
            self.status = "Issued"
            print("Success:", self.title, "has been issued.")
        else:
            print("Sorry,", self.title, "is currently issued to someone else.")
            
    def return_book(self):
        if self.status == "Issued":
            self.status = "Available"
            print("Success:", self.title, "has been returned.")
        else:
            print(self.title, "was not issued.")
            
    def show_info(self):
        print("Title:", self.title, "Author:", self.author, "Status:", self.status)

library = []

while True:
    print("\n--- Library Menu ---")
    print("1. Add a new book")
    print("2. Issue a book")
    print("3. Return a book")
    print("4. Show all books")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        t = input("Enter book title: ")
        a = input("Enter book author: ")
        new_book = Book(t, a)
        library.append(new_book)
        print("Book added successfully!")
        
    elif choice == '2':
        search_title = input("Enter title to issue: ")
        found = False
        for b in library:
            if b.title.lower() == search_title.lower():
                b.issue_book()
                found = True
                break
        if not found:
            print("Book not found in library.")
            
    elif choice == '3':
        search_title = input("Enter title to return: ")
        found = False
        for b in library:
            if b.title.lower() == search_title.lower():
                b.return_book()
                found = True
                break
        if not found:
            print("Book not found in library.")
            
    elif choice == '4':
        if len(library) == 0:
            print("The library is currently empty.")
        else:
            for b in library:
                b.show_info()
                
    elif choice == '5':
        print("Exiting Library Management System. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")