#wap to input the temperature in Farhenheit and print its equivalent  in centigrade
# c= (5/9) * (f-32)


temp_in_F = int(input("enter the temperature in farhenheit: "))

temp_in_C = (5/9) * (temp_in_F - 32)

print("the temperature in Centigrade is : ", temp_in_C)