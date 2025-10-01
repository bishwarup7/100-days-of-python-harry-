
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
