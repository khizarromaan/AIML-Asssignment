def manage_marks():
    marks = []
    
    while len(marks) < 5 :
        try:
            mark = float(input("Enter marks:"))
            marks.append(mark)
        except ValueError:
            print("Invalid input, Enter a Number:")
            
            
    total = 0 
    for i in marks:
     total = total + i
    
    avg = total/len(marks)
    
    print("Average: ", avg)
    print("Highest: ", max(marks))
    print("lowest: ", min(marks))
    
    marks.sort(reverse=True)
    print("Marks in descending order:",marks)
    
manage_marks()
    