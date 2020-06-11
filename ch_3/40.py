#wap to tabulate the function f(x) = (x sq. + 1.5x + 5)/(x-3) for x =-10 to 10.
#print both values of x and corresponding values of f(x)


x = int(input("enter the number: "))
for i in range(-10,11):
    f_x = ((x*x) + (1.5 * x) + 5)/ (x-3)

print(f_x)


