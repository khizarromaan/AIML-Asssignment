name = input("Enter your Name: ")
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

bmi = weight / (height ** 2) #bmi formula

print(name,"Your BMI is", round(bmi, 2))

#to round a number to only to float digit we use round(value, 2)