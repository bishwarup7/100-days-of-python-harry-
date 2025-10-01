
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
