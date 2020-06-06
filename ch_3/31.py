#two numbers and their LCM

'''
a = int(input("enter the first number: "))
b = int(input("enter the second numebr: "))
ls1 = []
ls2 = []

for i in range(1,a+1):
    if a%i == 0:
        ls1.append(i)

for i in range(1,b+1):
    if b%i == 0:
        ls2.append(i)

print(ls1)
print(ls2)

'''

a = int(input("enter the number: "))
ls = []
ls1 = []

for i in range(1,a+1):
    if a%i == 0:
        ls.append(i)


for i in ls:
    if i > 1:
        if i%2 != 0:
            ls1.append(i)

print(ls1)



    




