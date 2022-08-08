# Writting a program to check if the given year is a leap year or not
year = int(input("Enter The Year: ")) #Inputing the number
if (year%4 ==0 and year%100!=100) or (year%4 == 0): #using the if, and , or statements to simplify the process
    print(year, "it's a leap year") #conclusion if the following entered year is a leap year.
else: #using else in case it's not a leap year
    print(year, "It's not a leap year") #conclusion if the following entered year is not a leap year
