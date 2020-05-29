#wap to input a number and print the cube of its square root

from math import sqrt
a = int(input("enter the number: "))

square_root_of_a = sqrt(a)
cube = square_root_of_a * square_root_of_a * square_root_of_a

print("the cube of " + str(square_root_of_a) + " is: ", cube)