#first program

#string
print("hello World") #to print on the next line
print ("hello","diksha")

print("hello","diksha")  #to print on the same line

#integers
print(5)
print(5+10)



#variables
name = "diksha"
age = 19
price = 25.99

print("name") #value in "" is printed as it is
print(name)  #value of variable is printed

print("My name is :", name)
print("My age is :", age)


"""
Identifiers

A name used to identify a variable, function, class, module, or other object.
Must start with a letter or underscore (_), followed by letters, numbers, or underscores.
Case-sensitive.
"""

print("#Data Types")
#Python automatically detects the data type of the variable
# No need to explicitly declare data types

name = "diksha"  #string
age = 19         #integer
price = 25.99   #float

print(type(name))  #to check the data type of variable  
print(type(age))   #to check the data type of the variable
print(type(price))  #to check the data type of the variable



#Print Sum
a = 100
b = 50
sum = a + b
print(sum)

#Arithmetic Operators(+,-,*,/,%,**)
print("Arithmetic Operators(+,-,*,/,%,**)")
a = 100
b = 5

print(a+b)  #addition
print(a-b)  #subtraction
print(a*b)  #multiplication
print(a/b)  #division
print(a%b)  #modulus
print(a**b) #exponentiation

#Relational operators/Comparison Operators (==, !=, >, <, >=, <=)
print("#Relational operators")
a = 100
b = 50

print(a == b)  #equal to
print(a != b)  #not equal to
print(a > b)   #greater than
print(a < b)   #less than
print(a >= b)  #greater than or equal to
print(a <= b)  #less than or equal to


#Assignment Operators (=, +=, -=, *=, /=, %=, **=)
print("#Assignment Operators (=, +=, -=, *=, /=, %=, **=)")
a = 100

a += 10  # equivalent to a = a + 10
print(a)
a -= 5   # equivalent to a = a - 5
print(a)
a *= 2   # equivalent to a = a * 2
print(a)
a /= 2   # equivalent to a = a / 2
print(a)
a %= 3   # equivalent to a = a % 3
print(a)
a **= 2  # equivalent to a = a ** 2
print(a)


#Logical Operators (not, and , or)
print("#Logical Operators")

#Not operator: similar to negation in Logic Table
#And operator: similar to conjunction in Logic Table
#Or operator: similar to disjunction in Logic Table
a = 50
b = 100

print("Not operator:",not False)
print("Not operator:",not(a < b))
print("And Operator:",a < b and a != b)
print("And Operator:",a < b and a == b)
print("Or Operator:",a == b or a >=b)
print("Or Operator:",a == b or a <=b)



print("#Type Casting and type conversion")
"""
Type conversion : (implicit) python is a language tht "automatically" converts the type of the data as required
                    EG: int -> float
Type Casting: (Explicit) Refers to the explicit conversion "done by the user" using the built in functions such as int(), float(), str() etc to convert to another data type deliberately
"""
a = float("2")
b = 4.25
print(type(a)) #int deliberatelty became float
print(a+b)      #Python automatically recognizes the data type of the output
print(type(a+b))
a = 3.25
a = str(a)
print(type(a)) #float deliberately beacame string




print("#Input in Python")
"""
input() : fucntion used to take input from the user 
    **input datatype is always (str)**
    We need t0 type caste to take another datatype 
1. int(input())
2. float(input())

"""
name = input("Enter your name: ")
age = int(input("Enter your Age:"))
marks = float(input("Enter your marks:"))

print("welcome", name)
print(type(name),name)
print(type(age),age)
print(type(marks), marks)

#Lets Practice
print("Question 1")
val1 = int(input("Enter the first number:"))
val2 = int(input("Enter the second number:"))


print("sum:",val1 + val2)

print("Question 2")

a = float(input("Enter side of a square:"))
print("Area of square:", a ** 2) #a** 2 is a^2

print ("Question 3")
val1 = float(input("Num1 ="))
val2 = float(input("Num2 ="))

print("Average:", ((val1 + val2)/2))


print("Question 4")

a = int(input("Enter val of A:"))
b = int(input("Enter the val of B:"))

print(a>=b)