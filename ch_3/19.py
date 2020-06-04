#wap to input 1000 numbers and print the biggest number

list_of_numbers = [int(input("enter the number: ")) for x in range(5)]
large = 0

for i in range(len(list_of_numbers)):
    if list_of_numbers[i] > large:
        large = list_of_numbers[i]

print(large)
