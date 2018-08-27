'''
#Question1:->Name and handle the exception occured in the following program: 

    a=3
     if a<4:
        a=a/(a-3)
         print(a)
'''

#ZeroDivisionError

Solution:->
a=3
try:
    if a<4: 
        a=a/(a-3)
except:
    print(" divide by Zero error occurs....please enter value of a other than 3")
print()

'''
#Question2:->Name and handle the exception occurred in the following program: 
l=[1,2,3] 
print(l[3]) 
'''
#IndexError

Solution:->
l=[1,2,3] 
try:
    print(l[3])
except:
    print("Index out of range")
print()

'''
#Question3:->What will be the output of the following code:

    # Program to depict Raising Exception
     
    try:
        raise NameError("Hi there")  # Raise Error
    except NameError:
        print("An exception")
        raise  # To determine whether the exception was raised or not
'''
output is An exception
if we run the code below:->
 try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")

the exception was raised.

print()


'''
#Question4:->What will be the output of the following code: 

     # Function which returns a/b
    def AbyB(a , b):
        try:
            c = ((a+b) / (a-b))
        except ZeroDivisionError:
            print("a/b result in 0")
        else:
            print(c)
    
    # Driver program to test above function
    AbyB(2.0, 3.0)
    AbyB(3.0, 3.0)
'''
#Solution:->
-5.0
a/b result in 0
print()

'''
#Question5:->Write a program to show and handle following exceptions: 
1. Import Error 
2. Value Error 
3. Index Error  
'''
1.Import Error:->The ImportError is raised when an import statement has trouble
successfully importing the specified module.
Typically, such a problem is due to an invalid or incorrect path,
which will raise a ModuleNotFoundError in Python 3.6 .

#Example
try:
    import chirag
except ImportError as message:
    print(message)
print()


2.Value Error:->This error will occur when a user enter wrong input .Wrong input means
user can enter string value in case of an integer value. Example gives us a
perfect explaination.

#Example
marks=int(input("Enter a number"))
try:
    if(marks>40):
        print("Good student")
except :
    print("Below average student")
finally:
    print("End of Code!")
print()

3.Index Error:->This error will occur when we have a list containing 3 elements .
We all know list starts with 0(Zero index) if we want to access 3rd element so it
will present at index 2.And if we want to check at index 3 what value we have.At
that time the error occurs named as Index error.

#Example
listt=[1,2,3,4,5,6]
print(listt[6])
print()
        




