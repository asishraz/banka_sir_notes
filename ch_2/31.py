#wap to enter 2 operands and an operator (*,-,+,/) and display the calculated result


a = int(input("enter the first number: "))
b = int(input("enter the second number: "))


operator = str(input("enter the opeartor from '+','-','/','*': "))

if operator == "+":
    print("Addition of " + str(a) + " and " + str(b) + " is: ", a+b)
elif operator == "-":
    print("Subtraction of " + str(a) + " and " + str(b) + " is: ", a-b)
elif operator == "*":
    print("multiplication of " + str(a) + " and " + str(b) + " is: ", a*b)

elif operator == "/":
    print("Division of " + str(a) + " and " + str(b) + " is: ", a/b)
else:
    print("the operator is not valid")