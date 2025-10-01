
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