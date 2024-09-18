# #To print your name 
# print("Bharti is a good girl")
# # to print your name using input
# name= input("Enter your name:")
# print(name)
# # Write a Program to find the age 
# currentYear = int(input("Enter the current year"))
# bornYear = int(input("Enter the born year"))
# ageInYear = currentYear-bornYear
# print(ageInYear)
#WAP for currency convertor
# print("Convert rupees into dollars")
# rupeesAmount = int(input("Enter your amount in Rs."))
# rsIntoDollar = (rupeesAmount / 84)
# print(rupeesAmount ," convert into dollar " ,rsIntoDollar)
#Reverse converter
# print("Convert dollars into rupees")
# dollarAmount = int(input("Enter your amount in dollar"))
# dollarIntoRupees = (dollarAmount * 84)
# print(dollarAmount ," convert into rupees " ,dollarIntoRupees)
#WAP to check if you are eligible for voting or not using if else
# userAge= int(input("Enter your age here"))
# if (userAge > 17):
#     print("You are eligible for voting")
# else: 
#     print ("Not eligible for voting")
#WAP to check the user eligible for job
# if gender is female and age is greater than 17
#if gender is male then they can apply for pvt job
# userAge=int(input("Enter the user age"))
# userGender= input("Enter the gender ")
#WAY1 to solve
# if(userAge>17 and userGender=="female"):
#     print("You are eligible Govt job")
# elif(userAge>17 and userGender=="male"):
#     print("You are eligible Pvt job")
# else:
#     print( "Not eligible for job")
"""WAY2 to solve(incorrect code as per condition coz putting 
 anything also says eligible for Pvt job)"""
# if(userAge>17):
#     if(userGender=="female"):
#         print("You are eligible for Govt job")
#     else:
#         print("you are eligible for Pvt job")
# else:
#     print("You are not eligible for any job")
#Way 2 correct 
# if(userAge>17):
#     if(userGender=="female"):
#         print("You are eligible for Govt job")
#     elif(userGender=="male"):
#         print("you are eligible for Pvt job")
#     else:
#         print("your gender does not exist")
# else:
#     print("You are not eligible for any job")
#WAP to check the greatest number among 3 numbers
# a=int(input("Enter first number"))
# b=int(input("Enter second number"))
# c=int(input("Enter third number"))
#CAN BE WRONG as well concept
# if (a>b):
#     if (b>c):
#         print(a,"is the greatest number")
#         if(b<c):
#             print(a,"is the greatest number")
#             if(c>a):
#                  print(c,"is the greatest number")
#             else:
#                 print(a,"is the greatest number")
#         else:
#             print(c,"is the greates number")
#     else:
#         print(b,"is the greates number")
# else:
#     (b,"is the greatest number")
#correct way for greatest number
#a=7 b=9 c=4
# if(a>b and a>c):
#     print("A is greatest number")
# elif(b>a and b>c):
#     print("B is greatest number")
# else:
#     print("C is greatest number")
#switch condition is the replacement of multiple if else block
#List
# friendname= ["pawan","ivan"]
# # print(type(friendname))
# #print before add name
# #print("before",friendname)
# #to add the new friend name in the list
# friendname.append("Dil Bhardwaj")
# #print after adding the name
# #to add the name in the specific position
# #friendname.insert(0,"Harsh")
# #print after adding the name at 0 index
# #print("add name at index 0", friendname)
# #print(friendname)
# #list can have hetrogeneous elements and also duplicate data
# #array can only store homogeneous elements 
# # print(friendname)
# #for list method friendname._____
# #friendname.remove("Harsh")
# #print after removing name from the list
# #print(friendname)
# #to clear the list
# # friendname.clear()
# # print(friendname)
# #friendname.pop()#for removing the last element follow stack
# #print(friendname)
# #index number in pop (to remove the data in the list)
# # friendname.pop(2)
# # print(friendname)
# #to sort the list
# friendname.sort()
# print(friendname)
# #to print element of the given list
# for names in friendname:
#     print(names)
# #to print the number from 1 to 10 in ascending order
# for i in range(1,20):
#     print(i)
# #to print the 1 to 10
# for x in range(11):
#     print(x)
# # to print even numbers till 20 
# for y in range(1, 21):
#     if y % 2 == 0:
#         print(y)
# #another way
# for num in range(2, 21, 2):
#     print(num)
#tuples used to store the data and data is unchangeable
# sets= {"pawan","ivan","anshu","ivan"}
# #set.____for additional functions 
# sets.add("harsh")
# sets.remove("harsh")
# sets[0] ="bhs" #gives error 
# #we cannot modify the data in sets 
# print(sets)
#print(type(sets))
#set is unchangeable and unordered most rigid form
# friendname=["ram","shyam","gita","sita","kavita"]
# print(friendname)
# print(type(friendname))
# friendname.sort(reverse=True)
# print(friendname)
# friendname.clear
# print(friendname)
"""use while loop for printing 1 to 10"""
# Initialize the starting number
# num = 1
# # Loop until the number is greater than 10
# while num <= 10:
#     print(num)
#     num += 1  # Increment the number
#another way 
# i=1
# while i<11:
#     print(i)
#     i=i+1
# #reverse code
# # Initialize the starting number
# num = 10

# # Loop until the number is less than 1
# while num >= 1:
#     print(num)
#     num -= 1  # Decrement the number
#another function break 
# i=1
# while i<11:
#     print(i)
#     break
# i=i+1
# #another function continue 
# i=1
# while i<11:
#     print(i)
#     continue
# i=i+1
#another function continue changed sequence
# i=1
# while i<11:
#     i=i+1
#     print(i)
#     continue
"""Function in python, function main goal to reuse 
To reduce the code complexity """ 
# def myFunction():
#     print("my function called")
# #call the function by name 
# myFunction()
'''creating a function named as findArea through hieght and 
breath '''
# x=int(input("Enter the height here:"))
# y=int(input("Enter the breath here:"))
# def findArea(x,y):
#     z=x*y
#     print("area is",z)
# findArea(x,y)
#return z
# x=int(input("Enter the height here:"))
# y=int(input("Enter the breath here:"))
# def findArea(x,y):
#     return x*y
#     print("area is",z)
# area=findArea(x,y)
# print("the area is ", area)
"""WAP for N!(recursive function)""" 
def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Example usage:
n = 5
print(f"The factorial of {n} is {factorial_recursive(n)}")
'''Tuple- to donwload multiple unchangeable data
but it can be changed thorugh converting it into list first '''
# myTuple= ("Ivan","Anshu","Wani","Anjali","Wani")
#print(type(myTuple))
#print(myTuple) # printted 2 time Wani, can store duplicate 
#values alike the set
#value get stored with the index
#print(myTuple[1])
#myTuple[1]="Adarsh" # error as data can't be changed
# print(myTuple)
# # Define a tuple with 5 elements
# my_tuple = (10, 20, 30, 40, 50)
# # Use a for loop to iterate over each element in the tuple
# for element in my_tuple:
#     print(element)
# for x in my_tuple:
#     print(x)
#dict= it can store multiple data in key value pair
#e.g.
#name=Ashish
#email= ashish0@gmail.com
#mobile= 9898292939
# myDict={   
#      "name":"ashish tyagi",
#     "email":"ashish0gmail.com",
#     "mobile":"938934797"
# }
# print(type(myDict))
# print(myDict)
# for item in myDict:
#     print(myDict[item])
# print(myDict.get("email"))
# print(myDict.get("keys"))
# # myDict["name"]="Adarsh"
# # print(myDict)
# """OOPS"""
# '''Class and Objects'''
# #M must in capital rule in Mohit
# # class Mohit: 
# #     age= 20
# #     print("I am from Delhi")
# # x=Mohit()
# # print(x.age)
# # print(Mohit.age)
# '''Why we create class
# Class is a collection of functions, variable, objects or
# real world entities'''
# #car is a class and engine is a objects
# """Class is a collection of objects """
# '''class.object'''
# bornYear = int(input("Enter the born year:"))
# import datetime
# x= datetime.datetime.now ()
# # print(x.year)
# class  agecalculator:
#     age=x.year - bornYear
# m =agecalculator()
# print(m.age)
#polymorphism method overloading
# def age(dob1):
#     print(dob1)

# def age(dob, name):
#     print(dob, name)

# #x=age("19 oct 1999")
# y=age("20feb 2020", "Ashish")







