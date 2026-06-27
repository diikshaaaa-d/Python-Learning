print("Strings : \n String is a data type that stores a sequence of characters.")



print("\n")



str1 = "This is a string"
str2 = 'apna college'
str3 = """This is a string""" 

print("1] Escape sequence characters")

print("Next line:")
str4 = "This is a the first line.\nthis is the second line." #\n is for new line
print(str4)

print("Tab space:")
str5 = "this is the first line. \t this the second line." #\t is used for tab space
print(str5)



print("\n")



print("2] Basic Operations on strings") 

print("Concatnation : ")
first = "first word"
second = "second word"

print(first +" " + second) #concatenation of twoo strings

length = len(second) #length of the string
print(length) 



print("\n")



print("3] Indexing")

#Strings are indexed in Python, which means you can access individual characters using their position in the string. The index starts at 0 for the first character.
#you can only access the chaacters i python but you cannot change the characters in a string because strings are immutable in python

string = "apna college"

ch = string[0]
print(ch)
ch = string[1]
print(ch)
ch = string[2]
print(ch)
ch = string[3]
print(ch)
ch = string[4]
print(ch)
print(string[6])



print("\n")



print("4] Slicing of strings")

#Accessing a range of characters in a string is called slicing. The syntax for slicing is string[start:end], where start is the index of the first character you want to include, and end is the index of the first character you want to exclude.

string = "apna college"
print(string[0:4]) #slicing from index 0 to 3
print(string[:10]) #slicing from index 0 to 9
print(string[5:]) #slicing from index 5 to the end of the string
print(string[5:len(string)]) #slicing from index 5 to the end of the string



print("\n")



print(" 5] Negative Indexing ")

#Negative indexing allows you to access characters from the end of the string. The index -1 refers to the last character, -2 refers to the second last character, and so on.

string = "Apple" 
# A p p l e
# 0 1 2 3 4   Indexing from the start
#-5 -4 -3 -2 -1  Negative Indexing

print(string[-5:-1]) #slicing from index -5 to -2
print(string[-3:-1]) #slicing from index -3 to -2

print("\n")

print("6] String Funtions")

print("1.Endswith function : ")
#The endswit() function is used to check if a string ends with a specified suffix. It returns True if the string ends with the specified suffix, and false otherwise.

str = "My am studying python form apna college"

print(str.endswith("python")) #it returns false cus the string does not end with "python"
print(str.endswith(" apna college")) #it returns true cus the sring ends with "apna college")

print("2.Capitalize Funtion:")
#it capitalizes the first character of the string and converts the rest of the charachters to lower case.

str = "i am studying python from apna college"

print(str.capitalize()) #it capitalizes the first character of the string adnd converts the rest of the characters to lower case.

str = "diksha is my name."

str = str.capitalize()
print(str) #it capaitalizes the first character of the string and converts the rest of the characters to lower case and stores the new changes in the original string.

print("3.Replace Function : ")
#It replaces a specified old phrase with a new phrase in the string.The syntax is str.replace(old,new,count) where old is the phrase to be replaced, new is the phrase to replace it with, and count is an optional parameter that specifies the number of occurrences to replace. If count is not specified, all occurrences will be replaced.

str = "I am studying python from apna college." 
print(str.replace("python","java"))
print(str.replace("o","a"), str.replace("a","o")) 


print("4.Find Function :")
#The find() function is used to search for a specified substring within a string. It returns the index of the first occurrence of the substring if found, and -1 if not found. The syntas is str.find(substring, start, end), Where substring is the string to search for , start is the optional starting index to begin the search, and end is the optional ending index to limit the search.

str = "I am studying python from apna college."

print(str.find("diksha"))
print(str.find(" ",0,10)) #it returned me the space index
print(str.find("studying"))

print("5. Count Function :")

#It returns the number of occurences of a specified substring in the string. The syntax is str.count(substring, start,end) where substring is the string to count, start is the optional starting index to begin the count, and end is the optional ending index to limit the count.  

str = "I am studying python from apna college."

print(str.count("y"))
print(str.count("a",1,27)) 



print("\n")



print("Lets Practice some questions")

print("Qn.1] WAP to input users's first name and print its length.")

name = input("Enter your First name:")
print("Length of your first name :" , len(name))


print("Qn.2] WAP to find the occurent of '$' in a string")

str = "It costs $5 to buy me a cookie and $10 for a cake."
print(str.count("$"))
print(str.count("$",3,10))



print("\n")



print("7] Conditional statements")
#Conditional statements are used to perform different actions based on different conditions. In python, the main conditional statements are if, elif, and else.

print("1.if-elif-else")

#Light code example
light = "green"

if(light == "red"):
    print("STOP")
elif(light == "green"):
    print("GO")
elif(light == "yellow"):
    print("WAIT")

else:
    print("light is broken")

#Grading system

marks = int(input("Enter the marks:"))

if(marks >= 90):
    print("Grade = A")
elif(marks >= 80 and marks < 90):
    print("Grade = B")
elif(marks >= 70 and marks < 80):
    print("Grade = c")
else:
    print("Grade = D")

#secong method of writting the same code
if(marks >= 90):
    Grade = "A"
elif(marks >= 80 and marks < 90):
    Grade = "B"
elif(marks >= 70 and marks < 80):
    Grade = "C"
else:
    Grade = "D"

print("Your grade is : ", Grade)

#Nesting: one statement in another statement.
#IF->IF->print

age = int(input("Enter your age:"))

if(age >= 18):
    if(age > 80):
        print("Cannot drive")  #senior cirizen
    else:
        print("can drive") #ideal age
else:
    print("Cannot drive") #kids



print("\n")



print("Lets practice some qustions")

print("Qn.1] WAP to check if a number entred by the user is odd or even.")

number = int(input("Enter a number: "))
rem = number % 2
if(rem == 0):
    print("The given number is even")
else:
    print("The number is odd.")

print("Qn.2] WAP to find the greatest of 3 numbers entered by the user.")









