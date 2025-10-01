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