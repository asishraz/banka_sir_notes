#WAP to input the values of A and B and print the cube of their sum and the cube of their product

A = int(input())
B = int(input())
sum_of = A+B
mult = A*B
print("Cube: ", sum_of*sum_of*sum_of)
print("Cube(product): ", mult*mult*mult)