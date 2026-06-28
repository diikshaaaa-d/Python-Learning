#Lists in Python [] : A built in data type that stores set of values. It can store elements of diffrent types (integer, float, string,etc.)
print("syntax for lists: ")
marks = [99,88,98,91.2,67,98.9]

print(marks)
print(type(marks))
print(len(marks))
print(marks[3])



print("\n")


print("String VS lists")

string = "hello"
print(string[0])
#str[0] = "Y"  #not possible cause strings are immutable in python

#but Lists are mutable in python.
student = ["arjun" , 15 , 99.9 , "Mumbai"]
print(student[0])
student[0] = "Karan" #therefore we could change arjun to karan.
print(student)

#Error when you request access for the extra element of the string 
# print(student[7])  will give me error



print("\n")



print("List slicing")
#similar to string slicing
#syntax : list_name[staring_idx : ending_idx] #ending index is not included.

Marks = [87,64,33,95,76]
#        0, 1 , 2, 3, 4    index
#        -5,-4,-3,-2,-1    negative index
print(Marks[1:4])
print(Marks[:2])
print(Marks[1:])   #which is also same as marks[1:len(Marks)]
print(Marks[-4:-2])



print("\n")



print("List methods")
#  'list.'  gives me all the methods i need 

print("1] list.append()") 
#It adds the element in the bracet in the list at the end
#also called the mutation of the list.

list = [3,5,1]
list.append(9)
print(list) 

print("2.list.sort()    Ascending order :")
# sorts the list in asending and descending order.
#this one iss for ascending order.

list = [3,4,1]

list.append(10)
list.sort()

print(list.append(8)) #noting to return
print(list.sort()) #unlike string funtions, List methods does not return anything.

print(list)


print("3. list.sort(reverse=True)    Descending order: ")

list.sort(reverse = True)
print(list)

list = ["q","f","g","a","l"]

#sorts characters as well 
list.sort()
print(list)

print("4. list.reverse()")
#reverses the entire list
list = ["o","t","d","r"]
list.reverse()
print(list)

print("5. list.insert(idx,el)")
#idx is the place where you have to add an element
#el is the element you'll add in the list.

list = [ 2,4,6]
list.insert(2,7)
print(list)

print("6. list.remove()")
#remove first occurence of the given element

list = [3,6,3,7,8]

list.remove(3)
print(list)

print("7. list.pop() ")
#removes the element at given index

list = [3,6,3,7,8]
list.pop(3)
print(list)



print("\n")



print("Tuples in Python")
#A built in data type that lets us create immutable sequences of values. you cant change the values or add or remove values from tuples.

tup = (3,5,6,3,2)
print(type(tup))

print(tup[0])
print(tup[1])
print(tup[2])
# tup[0] = 3   #you cant change as tuple does not allow making changes , it is immutable.

tup = ()
print(tup)
print(type(tup))

tup = (1,) #Storing a single element in tuuple needs a comma, or else it is considered a variable string
print(type(tup))
tup = (1)
print(type(tup))
tup = (1.0)
print(type(tup))
tup = ("diksha")
print(type(tup))


print("Slicing in Tuples")

tup = (4,7,3,65,456,23,6)
print(tup[3:6])



print("\n")



print("Tuple Methods")

tup = (3,1,3,5,2,2)

print("1] tup.index(el) ")
# el =  is the element and this method returns the index of the firsr occurence.

print(tup.index(5))

print("2] tup.count()")
#el = the element whose total count is returned by the help of this method

print(tup.count(3))



print("\n")



print("LETS PRACTICE")

print("Qn.1] WAP to askt eh user to enter names of their 3 favorite movies and store them in a list.")


movies =[]

movies.append(input("first movie:"))
movies.append(input("second movie:"))
movies.append(input("third movie :"))
print(movies)


print("Qn2. ")
print("WAP to check if a list contains a palindrome of elements. Hint: use copy() method")
#what is palindrome? shuru se aur last se same hi hoti vo cheez [1,2,3,2,1] [a,b,a]

list1 = [1,2,1]
list2 = ["m","d","f","r","m"]

copy_list = list1.copy()
copy_list.reverse()

if(copy_list == list1):
    print("List is in palindrome")
else:
    print("Not in palindrome")

copy_list2 =list2.copy()
copy_list2.reverse()
if(copy_list2 == list2):
    print("List is in palindrome")
else:
    print("Not in palindrome")


print("Qn.3] WAP to count eh number of students with the 'A' grade in the following tuple")
grade = ["C","D","A","A","B","B","A"]

print(grade.count("A"))

print("Qn.4] Store the above values inn a list & sort them from 'A' to 'D'")

grade = ["C","D","A","A","B","B","A"]

grade.sort()
print(grade)

      