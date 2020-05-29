#wap to input a three digit number and print it in reverse order

digit = int(input("enter the three digit number: "))
sum_of_dig = 0 
rev = 0
count = 3

while count > 0:
    rev = digit % 10 #3 
    digit = digit // 10  #12
    sum_of_dig = sum_of_dig * 10 + rev #30
    count -= 1

print(sum_of_dig)
