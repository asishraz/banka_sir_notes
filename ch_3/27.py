#wap to input a number and print sum of its factors 


a = int(input("enter any number: "))
ls = []
total = 0

for i in range(1,a+1):
    if a%i == 0:
        ls.append(i)
print(ls)
for i in ls:
    total += i

print(total)