scores = [85, 92, 78, 92, 65, 92, 88]
print("index of 1st occurance of 92:",scores.index(92))
print("number of times 92 appears:",scores.count(92))

num = int(input("enter a number:"))
if num in scores:
     print("Index at which",num,"is present",scores.index(num))
     print("Times",num,"is repeated:",scores.count(num))   
else:
       print("Number not Found")
       