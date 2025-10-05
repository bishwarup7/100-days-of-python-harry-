
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