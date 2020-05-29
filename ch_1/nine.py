#wap to input the market price and discount of a two _wheeler and print the amount to be paid

market_price = int(input())
print("enter the discount down:")
discount = int(input())
discount_percent = (discount/100) * market_price

print("Amount to be paid: ", (market_price - discount_percent))