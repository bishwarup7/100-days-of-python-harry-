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