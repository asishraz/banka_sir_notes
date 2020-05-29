#wap to input length in metres and cm and print its equivalent length in feet
# 1ft = 12 in ; 1 in = 2.54 cm ; 100cm = 1m


measurement = float(input("enter the length: "))


to_cm = measurement * 100  #185cm
to_in = (1/2.54) * to_cm 
to_ft = (1/12) * to_in

print("the length in " + str(measurement) + " m and it will be in " + str(to_ft) + " ft. ")
