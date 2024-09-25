#calculator Last Take
from ast import Break
from time import sleep
import time 

print("Pick operation : ")
print("1 for add ")
print("2 for sub")
print("3 for multi")
print("4 for div")
print("1 or 2 or  3 or 4")
while True:
 choice = int(input("choose operand : "))
 if choice in (1,2,3,4):
    num1 = float(input("first number :"))
    num2 = float(input("second number : "))
    sum1 = num1 + num2
    sub1 = num1 - num2
    multi = num1 * num2
    div = num1/num2
 if choice == 1:
    print("Loading...")
    time.sleep(3)
    print("the sum is",sum1)
 if choice == 2:
    print("the diff is",sub1)
 if choice == 3:
    print("the product is",multi)
 if choice == 4:
    print("the div is",div)
 choice2 = input("Wanna continue(Y/N)? : ")
 if choice2 == "n":
   break
else:
    if choice !=  (1,2,3,4):
        print("invalid")