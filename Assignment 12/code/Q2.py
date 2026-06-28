def analyze_string(s):
    if s == "":
        print("string is empty")
        return
    
    print("length:",len(s))
    print("Reverse:",s[::-1])
    
    vowels = "aeiou"
    count = 0
    
    for i in s.lower():
        if i in vowels:
            count += 1
            
    print("Number of Vowels:", count)
    
    for i in range(len(s)):
        print("Character:", s[i],"Positive index:",i, "Negative index:",i - len(s))
        

text = input("Enter a string: ")
analyze_string(text)