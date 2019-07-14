import math
number = int(input("Enter the Number"))
num1=number+1

root = math.sqrt(num1)
if int(root + 0.5) ** 2 == num1:
    print(number, "is a perfect square")
else:
    print(number, "is not a perfect square")
