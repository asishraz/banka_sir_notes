#wap to input two numbers and print the sum of X% of first and Y% of second number

a = int(input("enter the first number: "))
b = int(input("enter the second number: "))

x = int(input("enter the X percentage: "))
y = int(input("enter the Y percentage: "))


x_of_a = (x/100) * a
y_of_b = (y/100) * b


total = x_of_a + y_of_b

print("sum of " + str(x) + " % of " + str(a) + " and " + str(y) + " % of " + str(b) + " equals: ", total)