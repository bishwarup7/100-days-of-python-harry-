
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
