'''
#day=5 [comments,ESCAPE SEQUENCES & PRINT STATEMENT
print("hey iam\" a \"good boy\"\n and this viewer is also a good boy/girl")
#ctrl+/ for multiple comment
print("hey",6,7,sep="~",end="009\n")

print("harry")
'''

'''
#day=6 [variable,data types
a9=123
print(a9)
a1 =9
b9 = "harry"
print(b9)
print(a9+a1)

a=1
b=True
c="Harry"
d=None
e=complex(5,6)
print("The Type of a is", type(a))
print("The Type of b is", type(b))
print("The Type of c is", type(c))
print("The Type of e is", type(e))
'''

'''a = 5
b = 45

print("The value of",a, " + ",3, "is:", a+b)
print("The value of",a, " - ",3, "is:", a-b)
print("The value of",a, " * ",3, "is:", a*b)
print("The value of",a, " / ",3, "is:", a/b)
'''
'''
#Calculator (exersice -1)
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Can't divide by zero."
    return x / y

print("select operation:")
print("1.add")
print("2.subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4): ")

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

if choice == "1":
    print("Result:", add(num1,num2))
elif choice == "2":
    print("Result:", subtract(num1,num2))
elif choice == "3":
    print("Result:", multiply(num1,num2))
elif choice == "4":
    print("Result:", divide(num1,num2))
else:
    print("Invalid input!")

'''
'''
#typecasting

str = "15" 
num = 7
str_num = int(str)

sum = num +str_num
print("The sum of both numbers:", sum)


'''
'''
#taking user input in python  day -10
x = input("Enter 1st number:")
y = input("Enter 2nd number:")

print(x+y)
print(int(x)+int(y))
print(int(x)+float(y))
print(int(x)+complex(y))
'''

'''
#exploring some functions:
a = input("Enter your name :")
print("My name is ", a)

x = input("Enter your first number :")
y = input("Enter your second number :")

print(x + y)

print(int(x) + int(y))
print(float(x) + float(y))
print(str(x) + str(y))
print(ord("W"))
print(hex(69))
print(oct(53))
print(tuple(x) + tuple(y))

s = set("jeep")
print(s)
print(list(x) + list(y))
info = dict(name="dipto", age = 22, city = "munich")
print(info)

'''
'''
#String are immutable day-13

a = "!!!Dipto!!!!!!!!!!!!!!Dipto"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Dipto", "bindiya"))
print(a.split(" "))
blogHeading = "introduction to js"
print(blogHeading.capitalize())

str1 = "welcome to the console!!!!!"
print(str1.center(50))
print(len(str1.center(50)))
print(a.count("Dipto"))

str1 = "welcome to the console!!!!!"
print(str1.endswith("!!!"))
str1 = "welcome to the console!!!!!"
print(str1.endswith("to", 4,10))


str1 = "he's name is Dan.He is an honest man."

print(str1.find("is"))
#print(str1.index("ishh"))

str1 = "welcome "
print(str1.isalnum())

str1 = "hello world"
print(str1.islower())

str1 = "we wish you a merry christmas\n"
print(str1.isprintable())

str1 = "                  "
print(str1.isspace())

str1 = "world health organization"
print(str1.istitle())

str1 = "python is a interpreter Language"
print(str1.startswith("python"))


str1 = "python is a interpreter Language"
print(str1.swapcase())

str1 = "he's name is Dan.He is an honest man."

print(str1.title())

'''
'''
#if -else day 14
appleprice = 10
budget = 200

if (budget - appleprice > 50):
    print("Stella, add 1 kg apples to the cart.")

elif(budget - appleprice > 70):
    print("It's ok you can buy.")

else:
    print("Stella, do not add apples to the cart.")


num = int(input("Enter a number:"))

if num < 0:
    print("Number is negative.")
elif ( num == 0):
    print("Number is zero.")
else:
    print("Number is positive.")

#nested if --- else

num = 18
if (num < 0):
    print("Number is negative.")

elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

'''
'''
#Good morning sir (excersice- 2) day 15
import time

timestamp = time.strftime("%H:%M:%S")
print(timestamp)
timestamp = int(time.strftime("%H"))
print(timestamp)
timestamp = int(time.strftime("%M"))
print(timestamp)
timestamp = int(time.strftime("%S"))
print(timestamp)


HOUR = int(time.strftime("%H"))

if 5 <= HOUR < 12:
    print("Good Morning!")
elif 12 <= HOUR < 17:
    print("Good Afternoon!")
elif 17 <= HOUR < 21:
    print("Good Evening!")

else:
    print("Good Night!")


from datetime import datetime

current_hour = datetime.now().hour

if 5 <= current_hour < 12:
    print("Good Morning!")
elif 12 <= current_hour < 17:
    print("Good AFternoon!")
elif 17 <= current_hour < 21:
    print("Good Evenning!")
else:
    print("Good Night!")

'''
'''
#match case statement day 16

x = int(input("enter the value of x :"))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    case _ if x!=80:
        print(x, "is not 90" )
    case _ if x!=90:
        print(x, "is not 80" )
    case _ :
        print(x)
'''
'''
#for loop day 17

name = "Bishwarup"

for i in name:
    print(i)
    if (i =="w"):
        print("hallo")


colors = ["red","green","blue","gold"]
for color in colors:
    print(color)
    for i in color:
        print(i)

for x in range (1,15,2):
    print(x)


n = 5
for x in range(n+1):
    print(x * "*")

n = 9
for x in range(1,n+1):
    print(" " *(n-x)+"*"*x)


n = 50

for x in range (1,n+1,5):
    print(x * "*")
'''
'''
#while loops in py day 18
count = 15
while(count > 0):
    print(count)
    count = count -1


i = int(input("enter the number:"))

while(i<=38):
     i = int(input("enter the number:"))
     print(i)
print("Done with the loop.")
'''
"""
#break and continue in py day 19

for i in range(12):
    if (i==10):
        break
    print("5 X",i+1,"=",5*(i+1))

print("lopp ended.")

for i in range(12):
    if (i==10):
        print("skip the iteration.")
        continue

    print("5 X",i+1,"=",5*(i+1))


i = 0 
while True:
    print(i)
    i = i+1
    if (i%100 == 0):
        break

"""
'''
# functions in python day 20
def calculategmean(a,b):
    m = (a*b)/(a+b)
    print(m)
def isgreater(a,b):
    if(a>b):
        print("a is greater than b")
    else:
        print("b is greater than a")

def islesser(a,b):
    pass

a = 5
b = 8
isgreater(a,b)
calculategmean(a,b)

c=15
d=58
isgreater(c,d)

calculategmean(c,d)

'''
'''
#function argument 21 day
def average(a,b,c=1):
    print("The average is",(a+b+c)/2)
average(5,6)


def average(*numbers):
    sum=0
    for i  in numbers:
        sum = sum+i
    print("The average is:", sum/len(numbers))
average(5,6)

def average(*numbers):
    sum=0
    for i  in numbers:
        sum = sum+i
    return sum/len(numbers)
    return 7 #ignore
c=average(5,6,7,1)
print(c)
'''
'''
#introduction to list in python day 22

marks = [3,5,7,"Bindia",True,6,2,58,593,57]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
#print(marks(5))

print(marks[-3])            #Negative index
print(marks[len(marks)-3])            #positive index
print(marks[5-3])        #positive index
print(marks[2])       #positive index

if "7" in marks:
    print("yes")
else:
    print("no")

#same thing applies for strings as well!
if "Bin" in "Bindia":
    print("yes")

print(marks)
print(marks[1:-8])
print(marks[1:8:3])

#list comprehension
lst = [i*i for i in  range(10)]
print(lst)
lst = [i*i for i in  range(10) if i%2==0]
print(lst)
'''
'''
# list method in py 23 day

l = [89,54,25,1,2,1,3,4,6]
print(l)
l.append(9)
l.sort()
print(l)
l.sort(reverse=True)
print(l)
l.reverse()
print(l)
print(l.index(1))
print(l)
print(l.count(1))
print(l)
m = l.copy()
m[0] = 0
print(l)
l.insert(1,6969)
print(l)

m =[900,1000,1500]
l.extend(m)
print(l)
'''
'''
#tuples in py day 24

tup = (1,2,54,6,54,5)
print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])

if 96 in tup:
    print("yes 96 is present in this tuple")
tup2 = tup[1:4]
print(tup2)
'''
'''
#operations on tuples in py day 25

countries = ("Japan","Brazil","Russia","Germany")

countries2 = ("Korea","Argentina","USA","France")


earth = countries + countries2
print(earth)

countries = ("Spain","Italy","India","England","DRC")
trp = list(countries)
trp.append("scotland")
trp.pop(3)
trp[2] = "Iran"
countries = tuple(trp)
print(countries)

tuple1 = 0,1,2,31,2,3,1,2,3
rep = tuple1.count(3)
rep = tuple1.index(3,4,8)
res = len(tuple1)
print("Count of 3 in tuple1 is:",rep)
'''
'''
#Exercise 2: solution & shoutouts 26 days

import time
ok = time.strftime("%H:%M:%S:")
hour = int(time.strftime("%H:"))
hour = int(input("Enter the hour:"))
print(hour)

if (hour >= 0 and hour < 12):
    print("Good Morning!")
elif (hour >= 12 and hour <17):
    print("Good Afternoon!")
elif ( jour >= 17 and hour < 0):
    print("Good Night!")
'''

#Kaun Banega Crorepati  27 days
'''
#F-string 28 days

country = "Germany"
name = "Bishwarup"

print(f"hey my name is {name} and I'm from {country}")

price = 100.05637
txt = f"For only {price:.2f} dollars!"
print(txt)

print(type(f"{2*30}"))

country = "Germany"
name = "Bishwarup"

print(f"hey my name is {{name}} and I'm from {{country}}")
'''
'''
#Docstrings in python 29 days

def square(n):
    Takes in a number n, returns the square of n {comment korte hobe ai line }
    print(n**3)
square(2)
print(square.__doc__)
'''
'''
#Recursion in python 30 days

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(3))
print(factorial(4))
print(factorial(5))



def fibonacci(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return (n-1) + (n-2)
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
'''

'''
#sets in python  31 days
s= {2,4,2,6}
print(s)

info = {"carla","ester",19,5.6,19}

print(info)

ken = set()
print(type(ken))

for value in info:
    print(value)
'''
'''
#set methods in python 32 days

s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)

cities = {"Munich", "Paris","Rome","Lisbon"}
cities2 = {"Munich", "London","Brussels","Paris"}

cities3 = cities.intersection(cities2)
print(cities3)

cities.intersection_update(cities2)
print(cities)


cities = {"Munich", "Paris","Rome","Lisbon"}
cities2 = {"Munich", "London","Brussels","Paris"}

cities3 = cities.symmetric_difference(cities2)
print(cities3)


cities = {"Munich", "Paris","Rome","Lisbon"}
cities2 = {"London","Brussels","prague"}

cities3 = cities.difference(cities2)
print(cities3)


cities = {"Munich3", "Paris9","Rome","Portugal"}
cities2 = {"Munich", "London","Brussels","Paris"}

cities3 = cities.isdisjoint(cities2)
print(cities3)


cities = {"Munich", "Paris","Rome","Portugal"}
cities2 = { "London","Brussels"}
print(cities.issuperset(cities2))
cities3 = {"Paris","Rome","Portugal"}
print(cities.issuperset(cities3))
print(cities3.issubset(cities))

cities2 = {"London","Brussels","prague"}

cities.add("Madrid")
print(cities)


cities = {"London","Brussels","prague"}

cities.remove("London")
print(cities)


cities = {"London","Brussels","prague"}

cities.discard("London2")
print(cities)


cities = {"London","Brussels","prague"}

item = cities.pop()
print(cities)
print(item)


cities = {"London","Brussels","prague"}
del cities
print(cities)

'''

'''
#Dictionaries in pyhton 33 days

dict = {
    69: "Dipto",
    96: "Bindiya",
    55: "Susmita",
    21: "Ritu"
}
print(dict[55])

info = {"Name":"Karan","Age":20,"eligible":True}
print(info)
print(info.keys())

for key in info.keys():
    print(f'The value corresponding to the key {key} is {info[key]}')

print(info.items())
for key, value in info.items():
    print(f'The value corresponding to the key {key} is {value}')

'''
'''
#Dictionary methods in python 34 days

of1 = {122: 45, 123: 89, 547: 96, 589: 96}

of2 = {222: 67, 566: 90}

#of1.update(of2)
#of1.clear()
print(of1)

empt = {}
print(empt)

of1.pop(122)
print(of1)

of1.popitem()
print(of1)

#del of1

del of1[122]
print(of1)
'''
'''
#for loop with else in python 35 days
for i in range (6):
    print(i)
    if i ==4:
        break

else:
    print("Sorry no i.")


i = 0
while i <7:
    print(i)
    i = i+1
    #if i ==4:
     #   break

else:
    print("Sorry no i.")

for x in range(5):
    print("iteration no {} in for loop".format(x+1))
else:
    print("else block in loop ")
print("out of loop.")

'''
#Exception handlung in python 36 days
'''''
a = int(input("Enter the 1st number:"))
print(f"Multiplication table of {a} is : ")
try:
   for i in range(1, 11):
    print(f"{a} x {i} = {int(a)*i}")
except Exception as e:
    print("Invalid input!")

print("Some important message.")
print("End of program.")


try:
    num = int(input("Enter an integer:"))
    a [6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")

except IndexError:
    print("Index Error.")

'''
'''
#Finally keyword in python 37

def fun1():
    try:
        l = [1,5,8,6]
        i = int(input("Enter the index:"))
        print(l[i])
        return 1 
    except:
        print("Some error occured.")
        return 0 
    #finally:
    #    print("I am always executed.")

x = fun1()
print(x)
'''
'''
#Raising coustom errors in py 38 days

a = int(input("Enter any value between 5 and 9: "))

if (a<5 or a>9 ):
    raise ValueError("Value should be between 5 and 9.")


a = input("Enter the text : ")

if(a.lower() == "quit"):
    print("code runs well.")
else:
    raise ValueError("The input should be quit.")
'''
'''
#kaun banega crorepati exercise 3 days 39

questions =[
    [
        "what is the capital of Germany?", "Mossow", "Berlin", "Brussels", "Warsaw", "None", 4
    ],
    [
        "what is the capital of Germany?", "Mossow", "Berlin", "Brussels", "Warsaw", "None", 4
    ],
    [
        "what is the capital of Germany?", "Mossow", "Paris", "Brussels", "Warsaw", "None", 4
    ],
]
levels = [1000,2000,3000,4000,5000,10000,20000,40000,80000,160000,320000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for RS.{levels[i]}")
    print(f"a. {question[1]}                      b. {question[2]} ")
    print(f"c. {question[3]}                    d. {question[4]} ")
    reply = int(input("enter your answer (1-4): or 0 to quit"))
    if (reply == 0):
        money = levels[i-1]
        break
    if(reply == questions[-1]):
        print(f"Correct answer, you have won  RS. {levels[i]}" )
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 320000
        elif (i == 14):
            money = 10000000
    else:
        print(f"Wrong answer!")
        break
print("your take home money is {money}")
'''
'''
#Short hand if else statement 41 days

a = 3303
b = 3303

print("A") if a>b else (print("=") if a==b else print("B"))

#c = 9 if a>b else 0
#print(c)
'''
'''
#Enumerate function in py 41 days

marks =[12,54,65,87,92,1,23,33]
index = 0 
for mark in marks:
    print(mark)
    if(index == 3):
        print("Harry, awesome!")
    index += 1

marks =[12,54,65,87,92,1,23,33]
for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("Harry, awesome!")


marks =[12,54,65,87,92,1,23,33]
for index, mark in enumerate(marks, start=1):
    print(mark)
    if(index == 3):
        print("Harry, awesome!")
'''
'''
#how import works  in py 43 days
import math
result = math.sqrt(9)
print(result)

from math import sqrt,pi
result = sqrt(9) * pi
print(result)


import math as m
result = m.sqrt(9) * m.pi
print(result)

import h2
import math
print(dir(math))
print(math.nan, type(math.nan))
h2.welcome()
print(h2)

'''

'''
#days 44 how import works in py
from math import pi,sqrt
from math import pi, sqrt as s
import math as m
ok= m.s(9)*m.pi
print(ok)


import math
print(dir(math))

#from herry1 import welcome,herry
import herry1 as hr
import math
print(dir(math))
print(math.nan,type(math.nan))y
hr.welcome()
print(hr.herry)
'''
#days 45 is in we.py & com.py
#days 46 is os module but the lesson in complex so that why that code is not here
#days 47 is exercise so skip
'''
#days 48 local & global variables

x = 4
print(x)

def hello():
    x= 5

    print(f'The local x is {x}')
    print('hello,jonas')
print(f'The global x is {x}')
hello()
x = 5
print(f"the global x is {x}")

x = 10
def my_fun():
    global x
    y=5
    x=4
    print(y)
my_fun()
print(x)
'''

'''
#days 49 file io in py
#reading a file:
f = open('myflie1.text',"r")
text = f.read()
print(text)
f.close()

f = open('myfile2.txt', "w")
f.write("USSR, PRIVET I'm dipto")
f.close()

# with open('myfile2.txt', "w") as f:
#     f.write("USSR, PRIVET")


f=open("myfile2.txt","a")
f.write(" hello, germany")
f.close()
'''

'''
#days-50 read(),readlines(), and other methods
#
# f = open("my-file.txt","r")
#
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         print(line,type(line))
#         break

#[ this text should open in another text file to read/write op
#I wanna be a top rated CP.
#also become a ctf player.
#dream to go canada.]

with open("my-file.txt", "r") as f:
    i = 0
    while True:
        line = f.readline()
        if not line.strip():
            break
        i += 1
        parts = line.strip().split(",")

        if len(parts) < 3:
            print(f"Line {i} has missing data: {line.strip()}")
            continue

        m1, m2, m3 = parts[0], parts[1], parts[2]
        print(f"Marks of student {i} in Math is {m1}")
        print(f"Marks of student {i} in English is {m2}")
        print(f"Marks of student {i} in ICT is {m3}")
        print("---")


with open('my-file.txt','w') as f:
    lines = ['line 1\n', 'line 2\n', "line 3\n"]
    f.writelines(lines)
'''
























