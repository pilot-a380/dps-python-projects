# Write a program to accept percentage of a student and display corresponding grade based on the criteria specified in the table given below
# percentage is equal or more than 90 = grade A
# percentage is between 80 and 89 = grade B
# percentage is between 70 and 79 = grade C
# percentage is between 60 and 69 = grade D
# percentage is between 50 and 59 = grade E
# percentage is below 50 = grade F 

percentage = int(input("Enter the obtained precentage: "))

if (percentage >=90):
    print("Your grade is A") 
elif (percentage >=80 and percentage <90):
    print("Your grade is B")
elif (percentage>=70 and percentage <80):
    print("Your grade is C ")
elif(percentage >=60 and percentage <70):
    print("Your grade is D ")
elif(percentage>=50 and percentage <60):
    print("Your grade is E ")
else:
    print("Your grade if F ")
