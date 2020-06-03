#wap to input 20 numbers and print the sum of numbers greater than 100

user_input = [int(input("enter the number: ")) for i in range(5)]

for i in user_input:
    if i + (i+1) > 100:
        print(i)
        continue

