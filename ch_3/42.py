#wap to print all the three digit numbers where the first digit is odd,
#second is divisible by 5
# and third is even 


'''
154
306
552
'''
last_digit = 0
mid_digit = 0
first_digit = 0
rev = 0
total = 0

for i in range(100,1000):
    last_digit = i % 10
    mid_digit = (i//10)%10
    first_digit = (i//10)//10

    if first_digit % 2 != 0 and mid_digit % 5 == 0 and last_digit % 2 == 0:
        print(i)
        # print(first_digit,mid_digit,last_digit)



    