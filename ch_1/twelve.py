#cost of each shirt in a shop is rs.500 only. The shop is giving a special festive discount  of 12.5% of each shirt.
#wap to input the number of shirts purchased and print the amount payable


shirt_cost = 500
discount_percent = 12.5

number_of_shirts = int(input())

total = shirt_cost * number_of_shirts

amount_payable = (discount_percent/100) * total

print("Amount payable is: ", amount_payable)
