text = input("Enter a String: ")

length = len(text)

print("length:",len(text))
print("last character:",text[len(text)-1])
#len()-1 for the last index because len() is o more than the last index of the string

if length % 2 != 0:
    print("Middle character of string: ",text[length//2])
    