#pefect number = sum of its factors excluding the number itself equals the numbers
#e.g = 6 -> 1+2+3 = 6


#wap to input a number and print whether it is perfect or not

ls = []
a = int(input("enter the number: "))
total = 0

for i in range(1,a):
    if a%i == 0:
        ls.append(i)

for i in ls:
    total += i

if total == a:
    print("the number " + str(a) + " is perfect...")
