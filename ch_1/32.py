#wap to enter the amount of purchase and print the amount payable. if the shopkeeper gives a discount of 50% + 40%
#this means, first we get a 50% discount on MRP and then 40% on the remaining value that you have to pay after the discount


amount = int(input("enter the amount: "))

first_50_percent = (50/100) * amount

remaining_val = amount - first_50_percent

final_40_percent = (40 /100) * remaining_val

print("first the amount was: ", amount)

print("then after 50% of discount, it went down to : ", first_50_percent)

print("then the value after 40% on remaining values changes to : ", final_40_percent)