"""
================

This file covers data types, comments, variables & printing, 
console input, arithmetic operators, type conversions, 
conditions, compound conditions, conditionals

================

* * * DATA TYPES * * * 

Data types are a way of classifying information. They can and do 
vary from programming from language to language.


** Core Data Types in Python: 

* int - any whole number that doesn't contain any decimal places. 

* float - any number that has a decimal part. Python will also 
treat 5.0 as a float, even though there is nothing substantial
in the decimal part. The fact that it has a decimal point
makes it a float as far as python is concerned 

* str - anything that is surrounded by double or single quotation marks. 
It is a best practice to always use double quotation marks 

It can be numbers or symbols surrounded by quotation marks, 
that is still a string 

* bool - True and False. Must be capitalized. 

* None - datatype is none, value is none. Used to signify nothing. 


** Using Print and Type to Find Out the Data Type

print(type(variable)) will print the type of an object


* * * COMMENTS * * * 

Convention is one space after the hash for comment, and 
if its on the same line on a statement, then place the hash
2 spaces after the statement: 

print("hello")  # prints hello 

Comment on complex code, and where it makes sense to



* * * PRINTING * * * 

print()

the print function can take multiple arguments, seperated by commas. 

print will automatically add a space between values seperated by commas 

print will also automatically create a new line after printing 

this happens like so:

print("hello", end='\n'), which is the same as print("hello", end="\n")

* Keyword argument

end="\n" is the default keyword argument to the print function

you can change that if you want multiple calls to the print 
function to be printed on the same line 


* * * VARIABLES * * * 

variables help us store data. 

syntax is 

variable_name = value 

name = "Jayant"


** Rules For Naming Variables 

* Start with a-z, capital or not, or an underscore _. 

* Make sure to make variables meaningful, not just 
x or y or x2. 

* You can have a number in the variable name

not at the beginning. 

* You can't have any special characters.

* You cannot have a space in the variable name.

* Variables are case sensitive

* Classes start with an uppercase, so regular 
variables should start with a lowercase 


** Camel Case and Snake Case

name_two is snake case 

nameTwo is camel case 

In Python, snake case is preferred 



* * * CONSOLE INPUT * * * 

Allows the user to type something in the console, and 
then use that info. 

For example, asking the user to give us their name. 

For this, we will use the function: 

input()

the input function takes one argument, a prompt, such as 

input("Please enter you name: ")

* The input function always stores the input data 
as a str datatype, regardless of what the user enters at the console 

this means that something like: 

age = input("enter your age ")

will have the age variable as a str datatype, even though
the user has input some integer on his end


** Input String Concatenation 

Take the following code as an example: 

name = input("Enter your name: ")

age = input("Hello, name, how old are you?: ")

Here, instead of the age prompt using the users inputted name
from the previous input statement, it will just print name 

and the input statement only takes one argument, so we can't 
have multiple arguments seperated by commas like we do 
for the print function. 

If we want to use the user's name in the age prompt, we 
have to use something called string concatenation.


name = input("what is you name?: ")

age = input("Hello, " + name + " what is your age?: ")

print(age)


The above code will have the desired result, as the concatenated string 
counts as one argument to the input function. 

Note that I have added space after Hello, and before what is
for the required spaces to show up in the prompt. 



* * * ARITHMETIC OPERATORS * * * 

Arithmetic operators are the operatoes we use on numbers, 
ie integers and floats. They include addition, subtraction,
division, multiplication, floor/integer division, 
and modulus. 

in the following code: 

x = y 

y = 4 

result = x + y  

x and y are the operands, and + is the operator

* Whenever there is a float involved in the operation
the result will be in data type float 

* When we are using the division operator, our result, 
no matter the data types of the operands, is going to be a
float 


** Exponential Operator 

x ** 2 

in python, that's x^2 


** Integer Division 

Gives the integer result from the division of values 

result = 5 // 2 

result == 2 

result = 3.5 // 4

result == 0 

Here, the ineteger part of the division is kept, and 
the decimal part is discarded 

However, in the case of the below code: 

result = 5.0 // 2.0 
print(result, type(result))

the value of result will be 2.0, and the datatype float, 
ie, even though the integer division is performed, the 
result, because of a float being used is a float. 

The same is true if either of the operands is a float 

Note: integer division does not round up. 3.6 will be 3. 


** Modulus 

result = x % y

Gives you the remainder after division of the operands. 

Here too, if either of the operands is a float, we 
will be returned the remainder as a float

result = 5.5 % 3.3

for the above code, for example, we will be returned 
a float with the value 2.2. So think of modulo as 

how many times does operand 2 go into operand 1 fully. 

** Note: just like in real life, you cannot divide
by 0 in python - it will return an error. 


** Order of Operations

The order of operations performed in pyhton is 

BODMAS or PEMDAS 

1. brackets/parentheses
2. exponents 
3. multiplication, division and mod 
4. addition and subtraction 

When multiple operations have the same precedence, 
they will be executed in the order they occur 
in the expression from left to right. 

** In Python, False is 0, and True is evaluated as 1, 
if ever used in an arithmetic operation 


** Multiplying Strings 

Other data types (other than ints and floats) cannot have
arithmetic operations performed on or with them. 

The exception is string, when ,multiplied by a numver will
be repeated that many times. For example 

"ABC" * 3 

will result in 

"ABCABCABC"

This particular string concatenation 
functionality is only available to python



* * * TYPE CONVERSIONS * * * 

Converting a value in one datatype to another datatype. 


** Converting Functions 

* int() - converts argument and returns an int value

x = int("4") will put the value 4 in x. 

y = int("4 hello") will throw an error 

y = int("4.5") will return an error, but float("4.5") will work

z = int(4.7) will work, and the value of z will be 4

* float()

float(4) will return 4.0 

float("4.5") will return 4.5

* bool()

bool("4") will return True 

That's because if a string has any contents in it, it will return true 

bool("") will return False, since its an empty string 

bool(" ") will return True, since there is a space and its not technically empty 

bool(0) will return True 

bool() with any other int or float passed in will return True 

* str()

str(0) will return "0"

str(23) will return "23"

str(True) will return "True"



* * * CONDITIONS * * *

An expression that evaluates to True or False.


** Conditional / Comparison Operators 

== and != operators 

cond = 2 == 3  # this expression will evaluate to False, stored in the variable cond

3.0 == 3  

will evaluate to True, even though we're comparing an int 
to a float. This is because when comparing, only the value will be compared 

3.0 != 3  

will evaluate to False. That's because we're asking if the two values 
are not equal, and they are. Thus: 

3.1 ! = 3  # will evaluate to True 


< and > operators 

x = 9
y = 4 

x + 2 > 9.5 

will return True, because whenever you do some arithmetic with 
regards to a comaprison, the arithmetic will be evaluated first, and then the 
comparison 

We can also use 

<= and >= operators 


** String Comparisons

x = 9 

x >= "6" 

will return an error, since you can't compare an int to a string 


x = 9 

x == "6" 
x != "6"

however will return False and True respectively, since they are not the same 
datatype, and thus not the same

str1 = "Hello" 
str2 = "hello" 

str1 == str2 

will return False, because of case sensitivity

str1 = "hello" 
str2 = "hello " 

str1 == str2 

will return False, because of the extra space in str2


** ASCII Comparisons 

str1 = "a" 
str2 = "b" 

str1 < str2 

will evaluate to True because of their ASCII values


** ord() and chr()

ord() will show you the ASCII/ordinal value of the argument

ord("a") will return 97
ord("A") will return 65

chr() will show you the char associated with an ordinal value 

chr(76) will return L 
chr(97) will return a

* Because of ASCII mappings, it's useful to remember that lowercase chars are 
greater than uppercase chars 


** String Comparison Evaluations 

When comparing strings, each char is evaluated at a time, and if they are equal
then pythin will move onto the next char. If one or the other is greater, it 
will declare the result. For example: 

str1 = "ABC"
str2 = "ABc" 

str1 >= str2 

Here, the first char of both strings are equal, so python will move to the second
char, which is also equal, so it will move to the third char. Here, "c" is greater
than "C", so the expression will evaluate to False 

True == 1
False == 0 

Will both evaluate to True



* * * COMPOUND CONDITIONS * * *

Conditions that involve multiple conditions to be evaluated 

** Logical Operators 

Operators that allow us to combine or chain conditions 

x = 2
y = 4

x < y and y + 2 > 3

will evaluate to 
True and True 
which means the compund condition evaluate to True 

and logical operator Truth table: 

True and True = True 
True and False = False 
False and True = False 
False and False = False 

We can chain more conditions like so: 

x = 2
y = 4

x < y and y + 2 > 3 and True 

This will also evaluate to True, however, 

x = 2
y = 4

x < y and y + 2 > 3 and False 

will evaluate to False, since all conditions here need to be True 
to finally evaluate to True 


** or logical operator

The or logical operator checks if either of the conmditions are True

x = 2
y = 4

x < y and y + 2 > 8

will evaluate to True, even though the condition on the right hand side is False 

or logical operator truth table 

True or False = True 
True or True = True
False or True = True 
False or False = False 

In chained conditions 

x = 2
y = 4

x > y and y + 2 < 8 and x == x

the following expression will evaluate to True, even though 
the first two conditions are False, since any one of the conditions 
need to be True for the whole condition to be evaluated as True


** not logical operator 

The not logical operator is a useful logical operator. It works by 
evaluating a particula condition, then giving us the opposite of the condition. 

not True = False 
not False = True 

x = 5
y = 6 

not (x > y) 

will evaulate to True, since (x > y) evaluates to False and not False is True

not True == False 

evaluates to False == False, which evaluates to True 

However, 

True == not False 

will return and invalid syntax error. This is because 
the == operator (and all comparison operators) have  
higher precedence than the not operator so python is trying to evaluate the 
whole condition before it has evaluated not False. To fix this, add parentheses: 

True == (not False) 

will return True 


** Order of Operations / Precedence for Logical Operators 

The order of operations is, in order: 

* Parentheses
* Conditional/Comparison operators 
* not 
* and 
* or


** De Morgan's Laws: 

not (x and y) == (not x) or (not y)

not (x or y) == (not x) and (not y)

 
* * * CONDITIONALS * * * 

* if statements 

if boolean:
    code

* else statement 

If you're going to use an else, you must have an if statement 
already defined above it

Good to use when you have usable condition, and one other statement

Else statement is not mandatory 

Anything indented to be under the 
else statement will come under that branch

* elif statement 

Need an if statement to work. Adds an additional check
besides the if statement 

Must come after an if and before an else 

Can have multiple elif statements as long as meeting above rules


** if statements can have compound conditions 

if number > 0 and number % 2 == 0:
    code

 
** One line if statement 

result = what you want for if true  condition  else what you want 

result = True if x > 5 else False 

result = "Ok" if x > 5 else "Not okay"

print("Hello") if x == "Okay" else print("Kuppa'd")












"""

from _typeshed import SupportsNoArgReadline


str = "this is me hello"

def reverse_string(string):
    list = []
    word = ""
    for i in string:
        if i == " ":
            list.append(word)
            word = ""
            continue
        else:
            word += i

    if word != "":
        list.append(word)

    list = list[::-1]

    print(list)

    result_str = ""

    for i in list:
        result_str += i + " "

    print(result_str)

reverse_string(str)



