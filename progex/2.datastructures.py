"""
* * * LISTS * * * 

Lists are a type of datatype in python.

they solve the problem of making many variables to store related numbers

A list is a collection of elements 

Instead of : 

x = 2 

x2 = 5

x3 = 6

x4 = 7 


* * Declaring a list 

x = []  # Declaring an empty list


* * Storing items in a list 

Lists can have ints, booleans, strings, floats and even lists inside 

x = [2, 5, 6, 7, True, 3.7, "hello]

* * Ordering 

The important thing about lists is that they are ordered. 
There is a first element, second element etc. 

The first element is at index 0, all the way up to 
n - 1, with n being the length of the list 

* * Accesing list elements 

name_of_list[index]

print(x[2])

Accessing an index that doesn't yet exist will throw an error


* * Changing elements to the list 

x[2] = 4
x[0] = True 


* * Adding elements to the end of a list

to append to the end of the list (add a new index)

abc = [0, 1, 2]

name_of_list.append(item)

abc.append("yes")

[0, 1, 2, "yes"]


* * List length 

Getting the length of a list uses the function len

len(collection object)

abc = [0, 1, 2, 3]

len(abc)

len works on other datatypes as well. 

such as a string, which is a collection of characters 

** Except with string, you can't modify the string in place, 
ie, you can't access the first element of the list and 
change it. But you can for a list. **


* * pop method 

pop will remove the last element from a list, and return it to you

x = [a, b, c, d]

x.pop()

[a, b, c]

popped = x.pop()
print(popped)
c

[a, b]


* * count method 

counts the total numbers of occurences of a passed in element

x = [1, 1, 2, 1, 4, 5, 2, 7]

count = x.count(1)

print(count)
3


* * index method

x.index()

will give you the index of the first occurence of the element passed in

x = [1, 1, 2, 1, 4, 5, 2, 7]

count = x.index(1)
print(count)
0

count = index(7)
print(count)
6

if you try and find the index of an element that's not in the list 
you'll get an error 

* * remove method 

will remove the first occurence of the passed in element from the list

x.remove()

if you try and remove an element that doesn't exist, you will get
thrown an error 

* * How to check if a list contains a particular element

* in operator 

abc = [1, 2, 3, 4, 5, 6, 7, 8]

contains = 5 in abc 
print(contains)
True

contains = "hello" in abc
print(contains)
False


* * Negative Index 

We can index the list from the end of the list 

We use a negative index to do this 

instead of 0, 1, 2, 3, 4, ... being the positive index counting
from the first element

for negative indexing we have -1, -2, -3 starting from right to left
or from the last element onwards 


abc = [33, 44, 23, 564, 76, 234, 87]
        0   1   2   3    4   5   6
       -7  -6  -5  -4   -3  -2  -1

* * With negative indexing, the first item in the list 
is negative number of items of the list 

So for a list with 8 items, positive index goes from 0 to 7
and negative index goes from -1 to -8 


* * Combining Lists 

* Way 1 - Addition operator 

x = [1, 2, 3]
y = [4, 5, 6]

combined = x + y
print(combined)
[1, 2, 3, 4, 5, 6]

This give sme a brand new list in combined, which tacks on y to x. 

* Way 2 - Extend a list 

x = [1, 2, 3]
y = [4, 5, 6]

x.extend(y)
print(x)
print(y)
[1, 2, 3, 4, 5, 6]
[4, 5, 6]

Here, x changes, since y is added onto it. 


* * Nesting Lists 

list = [[1, 2, 3], [4, 5, 6], [7, 8, 9, [10]]]

print(list[2][3][0])
10

* * List function 

list()

will take something and turn it into a list 








"""

# var = "kuppalatha"

# string1 = f"Hello, {5 + 1}, {var}"
# print(string1)

# state_capital_dict = {
#    "Tamil Nadu": "Chennai",
#    "Goa": "Panjim",
#    "MP": "Bhopal",
#    "UP": "Agra",
#    "Mizoram": "Aizawl",
#    "Kerala": "Trivandrum",
#    "Odisha": "Bhubhaneshwar",
#    "West Bengal": "Kolkata",
#    "Maharashtra": "Mumbai"
# }

lst = [1, 1, 1, 2, 3, 4, 3, 2, 4, 5, 4, 3, 5, 1]

counter_dict = {}

for i in lst:
    if i not in counter_dict:
        counter_dict[i] = 1
    else: 
        counter_dict[i] += 1

print(counter_dict)

list2 = list(counter_dict)
print(list2)