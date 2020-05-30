#wap to input three numbers and print the biggest number


a = int(input("enter the first number: "))
b = int(input("enter the second nunber: "))
c = int(input("enter the third number: "))

if a > b and a > c:
    print(str(a) + " is bigger ")
elif b > a and b > c:
    print(str(b) + " is bigger")
else:
    print(str(c) + " is bigger")


