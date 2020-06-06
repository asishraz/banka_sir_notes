#wap to input 1000 numbers and print the biggest as well as the second biggest number


user_input = [int(input("enter the number: ")) for x in range(5)]

user_input.sort()
a = user_input.pop()
b = user_input[0]

for i in range(len(user_input)):
    if user_input[i] > b:
        b = user_input[i]



print(a,b)

    
