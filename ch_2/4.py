#wap to input the weight of a person and print "overweight" if it is greater than 100. and print "underweight" if it less than 50
#otherwise print "normal weight"

weight = int(input("enter the weight in kg: "))

if weight > 100:
    print("overweight")
elif weight < 50:
    print("underweight")
else:
    print("normal weight")