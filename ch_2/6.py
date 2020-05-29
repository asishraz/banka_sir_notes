#wap to input a number and print whether the number is even or odd


a = int(input("enter any number: "))

if a%2 == 0:
    print("the number " + str(a) + " is even")
elif a%2 != 0:
    print("the number: " + str(a) + " is odd")