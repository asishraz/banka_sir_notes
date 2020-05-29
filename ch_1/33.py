#wap to enter the amount of purchase and print the amount payable if the shopkeeper gives a discount of 40% + 40% + 20%

amount_of_purchase = int(input("enter the amount of purchase: "))

first_40_percent = (40/100) * amount_of_purchase

first_deductions = amount_of_purchase - first_40_percent

second_40_percent = (40/100) * first_deductions

remaining_val = first_deductions - second_40_percent

final_20_percent = (20/100) * remaining_val
final_value = remaining_val - final_20_percent

print("the amount of purchase was: ", amount_of_purchase)
print("first, after 40% discount, the amount reduces to : ", first_deductions)
print("then, after 40% discount on the remaining value, the amount reduces to: ", remaining_val)
print("finally, after the 20% discount on the leftover, the amount payable is : ", final_value)

