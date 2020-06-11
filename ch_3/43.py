#wap to print all four digit numbers where the first two digits are even and the last two digits are odd

first_digit = 0
second_digit = 0
third_digit = 0
last_digit = 0
digit = 0


for i in range(1000,10000):
    last_digit = i % 10
    digit = i // 10
    third_digit = digit % 10
    digit = digit // 10
    second_digit = digit % 10
    digit = digit // 10
    first_digit = digit % 10
    if first_digit % 2 ==0 and second_digit % 2 == 0 and third_digit % 2 != 0 and last_digit % 2 != 0:
        print(i)

