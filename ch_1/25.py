#given y = (x_pow_6 + x_pow_4 + x_pow_2 + 10)/ (x_pow_5 + x_pow_3 + x)
#wap to enter the value of x and print the value of y

val_x = int(input("enter the value of x: "))

y = ((val_x * val_x * val_x * val_x * val_x * val_x) + (val_x * val_x * val_x * val_x) + (val_x * val_x) + 10) / ((val_x * val_x * val_x * val_x* val_x) + (val_x * val_x * val_x) + val_x)


print("the value of y is : ", y)