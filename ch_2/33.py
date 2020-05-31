#wap to enter the two digit number  and print whether it is palindrome or not

digit = int(input("enter the two digit number: "))

rev = digit % 10
new_digit = digit // 10

if rev == new_digit:
    print("the number " + str(digit) + " is palindrome")
    