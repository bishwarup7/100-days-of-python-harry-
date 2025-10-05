
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