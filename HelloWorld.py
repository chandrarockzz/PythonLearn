import this
from _ast import Add
from locale import str
import platform
import datetime

print('HelloWorld')
a = 10
print(a)
b = 11
print(b)
if a < b:
    print(a)
else:
    print(b)
sum = a + b
print(sum)
sum = (int)(100 / 3.0)
print(sum)
print(str(sum) + 'cha')
# print (sum+(int)('cha')) error
a = 1
b = 1
if a == b:
    print('equal')
elif a < b:
    print('a less than b')
elif a > b:
    print('a greater than b')
for i in range(2, 10, 3):
    print(i)
a = "Hello World Hello"
print(a[0])
print(a[1:6])
print(len(a))
for i in range(len(a)):
    print(a[i])
print(a.lower())
print(a.upper())
if a.islower():
    print("Yes lower")
else:
    print("No")
if a.count(a, 0, 3) == len(a):
    print("True")
else:
    print("False")

print(a.count("Hello", 0, 17))


# Functions-->>
def my_function():
    print('hai I am in FUnction')


my_function()


def my_string(b):
    print(b)
    return len(b)


print(my_string("Hello"))
print(my_string("World"))
print(my_string("Welcome"))
print(my_string("Me"))


def Add_Strings(a, b):
    return a + b


print(Add_Strings("Hello", "World"))
print(Add_Strings(1, 2))
print(Add_Strings(1.000, 3.000))

thislist = ["Hai", "Hello"]
print(thislist)
thislist[0] = "Hello"
print(thislist)
thislist[1] = "Hai"
print(thislist)


def SwapNumber(a, b):
    a = a + b
    b = a - b
    a = a - b
    print(a, b)


SwapNumber(10, 20)
SwapNumber(20, 10)


def Multiply(a, b):
    return a * b


print(Multiply(10, 20))
# Lists ------>>
# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
thislist = ["Applle", "Cherry", "Oranges"]
print(thislist)
print(thislist[0])
print(thislist[1])
print(thislist[2])
thislist[0] = "Hello"
print(thislist)
testlist = list(["Applle", "Cherry", "Oranges"])
print(testlist)
print(testlist.count("Cherry"))
testlist.append("Cherry")
print(testlist)
print(testlist.count("Cherry"))
print(len(testlist))
testlist.remove("Cherry")
print(testlist)
testlist.remove("Cherry")
print(testlist)
print(len(testlist))

# Tuple----->
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
thistuple = ("Hello", "World", "Hai")
print(thistuple)
print(thistuple.count("Hello"))
# thistuple[0] = "Hell" this is an error as tuple cant be changed
print(len(thistuple))

# Set
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
thisset = {"Hai", "Hello", "World"}
print(thisset)
print(len(thisset))
thisset.remove("Hai")
print(thisset)
thisset.add("How")
print(thisset)

# Dictionary
# A dictionary is a collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.
thisdict = {
    "Apple": "Green",
    "Banana": "yellow",
    "Mango": "yellow"
}

print(thisdict)
thisdict["Banana"] = "Green"
print(thisdict)
thisdict["Cherry"] = "red"
print(len(thisdict))
print(thisdict)
del (thisdict["Apple"])
print(len(thisdict))
print(thisdict)

i = 1
while i < 6:
    print(i)
    i += 1
i = 1
while i < 6:
    print(i)
    if i == 4:
        break
    i = i + 1

i = 0
while i < 6:
    i = i + 1
    if i == 4:
        continue
    print(i)

i = 0
while i < 100:
    i = i + 1
    if i == 50:
        continue
    print(i)

fruits = ["Apple", "Orange", "CHerry"]
for x in fruits:
    print(x)
for x in range(6):
    print(x)

for x in a:
    print(x)
for x in range(len(a)):
    print(a[x])

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Lambda Functions
#In python, the keyword lambda is used to create what is known as anonymous functions.
# These are essentially functions with no pre-defined name. They are good for constructing adaptable functions,
# and thus good for event handling.
myfunc = lambda i: i*2
print(myfunc(2))
myfunc = lambda x,y: x*y
print(myfunc(3,6))

def myfunc(n):
  return lambda i: i*n

doubler = myfunc(2)
tripler = myfunc(3)
val = 11
print("Doubled: " + str(doubler(val)) + ". Tripled: " + str(tripler(val)))

class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)

class MyDetails:
    def __init__(self, name , age):
        self.name = name
        self.age = age

p1 = MyDetails("Ramesh", 20)
print(p1.name)
print(p1.age)

class Test:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    def Name(self):
        print("My Name is "+ self.name)
p1 = Test("Chandra", 29)
p1.Name()

x = dir(platform)
print(x)

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.month)
print(x.day)