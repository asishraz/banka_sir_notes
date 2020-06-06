#wap to enter a number and check for its primness



a = int(input("enter any number to check: "))

ls = []


for i in range(1,a+1):
    if a%i == 0:
        ls.append(i)

count = 0

if len(ls) < 3:
    print("the number " + str(a) + " is prime.")