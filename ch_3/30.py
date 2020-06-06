#wap to enter two numbers and print their HCF


a = int(input("enter the first number: "))
b = int(input("enter the second number: "))


ls = []

if a < b:
    for i in range(1,a+1):
        if a%i == 0:
            ls.append(i)
    for i in ls:
        if b%i == 0:
            hcf = i

    
elif b < a:
    for i in range(1,b+1):
        if b%i == 0:
            ls.append(i)
    for i in ls:
        if a%i == 0:
            hcf = i




print("HCF of " + str(a) + " and " + str(b) + " is: ",hcf)


