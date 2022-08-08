#program to make a simple calculator

# This function adds two numbers
from operator import truth


def add(x,y):
    return x + y 

 #This function subtracts two numbers
def add(x,y):
    return x - y

#This function multiplies two numbers 
def multiply(x,y):
    return x * y

#This function divides two numbers
def divide(x,y):
    return x / y

print("Select Operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while truth:
    # Get to know what operation the user wants to do 
    choice = (input("Enter your choice(1/2/3/4)"))

    #check if the choice is one of the 4 options 
    if choice in('1','2','3','4'):
          num1=float(input("Enter the first number "))
          num2=float(input("Enter the second number "))

# proceed with furthur steps
          if choice == '1':
            print(num1 + num2, "Is your solution")

          elif choice == '2':
            print(num1 - num2, "Is your solution")
          
          elif choice == '3':
            print(num1 * num2, 'Is your solution')
           
          elif choice == '4':
            print(num1 / num2)

        # check if the user wants to do another calculation
        # break while loop is the answer is no
          next_calculation = input("Lets do another calculation (yes/no): ")
          if next_calculation == "no":
            break
else:
    print("Invalid input lol ")

