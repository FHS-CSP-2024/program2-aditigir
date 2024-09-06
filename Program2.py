# Information from the user #
#**Learning objectives**
#
#After this section:
#
#* You will know how to write a program which uses input from the user
#* You will know how to use variables to store input and print it out
#* You will be able to combine strings



## Live Demo ##
#
# Input from user
#name = input("What is your name? ")
#print("Hi there, " + name)
#
# Talk about Variables
#   * Note python is untyped and loose
#
# Reference a Var
#name = input("What is your name? ")
#print("Hi, ")
#print(name)
#print("!")
#print(name + " is quite a nice name.")
#
# Concat w/ +
#name = input("What is your name? ")
#print("Hi " + name + "! Let me make sure: your name is " + name + "?")
#
# Multiple Input
#name = input("What is your name? ")
#email = input("What is your email address? ")
#nickname = input("What is your nickname? ")
#print("Let's make sure we got this right")
#print("Your name: " + name)
#print("Your email address: " + email)
#print("Your nickname: " + nickname)
#
# Overriding Input
#name = input("What is your name? ")
#print(name)
#name = input("What is another name? ")
#print(name)



## Problem 1 ##
#Please write a script that: 
# - Asks for the user's name and then prints it twice, on two consecutive lines.
Name =input("What is your name?")
print(Name)
print(Name)




## Problem 2 ##
#Please write a script that: 
# - Asks for the user's name
# - Prints it out twice on a single line so that there is an exclamation mark at the beginning of the line, 
# - another between the two names and a third one at the end of the line.
Name = input("What is your name?")
print('!',Name,"!",Name,"!")

## Problem 3 ##
#Please write a script that: 
# - Asks for the user's name and address. 
# - The program should also print out the given information, as follows:
#   - Sample output
#   - First name: Steve
#   - Last name: Sanders
#   - Street address: 91 Station Road
#   - City and postal code: Folsom CA, 95630
FirstName = input("What is your first name: ")
Lastname = input("What is your last name: ")
Saddress = input("What is your street address: ")
Caddress = input("Enter the name of the city you live in: ")
staddress = input("Enter the name of the state you live in: ")
Paddress = input("What is the postal code of the area you live in: ")
print()
print("First Name:", FirstName)
print("Last Name:", Lastname)
print("Street address:", Saddress)
print("City and postal Code:",Caddress,'',staddress,',',Paddress )

#print(Name)
#print(adress)

## Problem ##
#Please write a script that: 
# - Asks for 3 words 
# - Puts the words together with dashes and prints that out
word1 = input("Enter your first word")
word2 = input("Enter your second word")
word3 = input("Enter your third word")
print(word1,word2,word3)
## Problem 5 ##
#Please write a script that: 
# - Asks for a name and a year
# - Prints out a short story that uses that information
Name= input("Enter your charecters name!")
Year=input("Enter a year!")
print(Name, "Was born in",Year,"And invented the flying car. The flying car is worth for 1 million dollers!" )
# Sample output:
#Please type in a name: Mary
#Please type in a year: 1572
# ----------------------------------------------
#Mary is a valiant knight, born in the year 1572. 
#One morning Mary woke up to an awful racket: a dragon was approaching the village. 
#Only Mary could save the village's residents. 
