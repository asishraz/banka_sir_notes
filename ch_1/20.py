#wap to input a number and print the cube of its square root of its cube root of its square root

from math import sqrt
num = int(input("enter any number: "))

square_of_num = sqrt(num)

cube_of_sqrt = square_of_num * square_of_num * square_of_num


square_of_cube_root = sqrt(cube_of_sqrt)

cube_of_final_sqrt = square_of_cube_root * square_of_cube_root * square_of_cube_root

print("the number is: ", num)

print("cube of its square root of its cube root of its square root is : ", cube_of_final_sqrt)

