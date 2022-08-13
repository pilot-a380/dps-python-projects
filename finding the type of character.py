#Python project to find the type of character if it is a alphabet or a number else a special character
#input the character


character = input("Please input any character: ")
if((character >= 'a' and character <= 'z' )) or ((character >= 'A' and character <= 'Z')):
    print("The Given Character is a Alphabet")
elif((character >= '0' and character <= '9')):
    print("The Given Character Is a Number ")
else:
    print("The Given Character is a special character ")

