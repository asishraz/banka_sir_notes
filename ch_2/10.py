#wap to input three numbers and print them in ascending order

a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))


if a < b and a < c:
    if b < c:
        print(a,b,c)
    elif c < b:
        print(a,c,b)

elif b < c and b < a:
    if c < a:
        print(b,c,a)
    elif a < c:
        print(b,a,c)

elif c < a and c < b:
    if a < b:
        print(c,a,b)
    elif b < a:
        print(c,b,a)


# ls = []

# ls.append(a)
# ls.append(b)
# ls.append(c)

# for i in ls:
    
