#wap to enter a two digit number and print its digits in reverse order

digit = int(input("enter any two digit number: "))
sum  = 1
count = 2
while count > 0:
    rev = digit % 10  #2
    new_dig = digit // 10 #1
    sum = rev * 10 + new_dig
    count -= 1


print(sum)



