"""
Programs often require us to store and manipulate data. 

PYTHON CORE DATA TYPES:

int  - any WHOLE number that doens't contain any decimal point. Positive or negative or 0. 

float - any number that contains a decimal point. 2.0 is also a float. .3 is also a float. -.7 is a float. 
8.89 is a float.

str - ANY sequence of characters surrounded by " " or ' ' quotation marks. "hello" is a string. 
"wv rf362kfc+/" is a string. "2" is a string. Anything wrapped 
in triple quotes """ """ or ''' ''' is also a string. 

bool - True or False. Capitalization is required. In python, True = 1 and False = 0; but do not 
go about assigning it so. 

None - used to signify nothing. 


TYPE FUNCTION 

print(type(object/variable)) will tell us the datatype of the input object. 

print(4) will return int, print ("hello") will return hello, etc. 


INTEGER / FLOOR DIVISION 

When we integer divide a float (11.0) by an int (3), and store that in a variable, 
the class of that variable will be float, not an it. In this case, it will be 3.0 

using the division operator will give you a float

whenever any operand is a float, the resulting datatype is float 

"""

# for i in range(4):
#     for j in range(4):
#         print(8, end = " ")
#     print(8)

# for i in range(3):
#     print("j loop begins for i,", i)
#     for j in range(3):
#         print(i, j)
#     print("j loop ends for i,", i)

'''
There is another kind of for loop in python that one can use - this is done so: 

for ch in "ABCDEFGH":
    print("char is", ch)
'''

# for ch in "ABCDEFGH":
#     print("char is", ch)

# #interesting behavior seen on this one
# for i in "1, 2, 3, 4, 5, 6, 7":
#     print("i is now", i)

# for i in "123456789":
#     print("i is now", i)

'''
While loops in python work like this: 

while(boolean):
    code


since there is no do while loop in python, you have to use: 

while True:
    code
    break out condition 

the difference between while loops and for loops: 

1. for loops are always finite. You can have a very large for loop, but it won't be infinite. 
2. while loops can do exponential stuff. For example, the following loop

exponent = 2
while (exponent < 10000)

exponent *= 3 

here, i will get 3, 6, 18, 54, etc. 

This kind of exponential calculation is very difficult to do with a for loop. Is it impossible? 
I don't know, and worth doing the math to find out. 



Occasionally, I won't want to traverse the entire length of an array or list. Here, I can use the 

break

keyword, which will break me out of a loop. Break can only be used inside a loop. It will 
break the nearerst loop it is a part of. 


'''

# for i in range(0, 100):
#     if i == 5:
#         print("found")
#         break
#     else:
#         print("not found")


'''
continue is another keyword that we can use, that when encountered within a loop, will take 
the control back to the beginning of the loop
ignoring the lines of code below it. Just like with break, continue will restart the loop it is closest to. 

For example: 
'''

# for i in range(0, 10):
#     if (i < 5):
#         continue
#     print(i)

'''
The above lines of code will not print i from 0 to 4, and will print i from 5 to 9.
'''

# given n, print the sum of cubes of all the numbers from 1 to n. 
# suppose n == 5 

# sum = 0
# n = 1
# while n < 6:
#     temp = n**3
#     sum += temp
#     n += 1

# print(sum)

"""
Functions - are constructs available in programming languages with which 
we can reduce duplicacy in code and 
make your code easier to understand. Through Functions we wrap our code in small bodies 
which we will be invoking or calling.  

Here is the syntax for functions in python:

def name_of_function():
    code

Well named functions are really rally useful in making code much more readable, smaller and more manageable
because they abstract away all the lines of code that don't need to be visible to muddy up the entire program

"""

def greet():
    print("Hello, world!")
    print("Welcome to the class")

greet()


