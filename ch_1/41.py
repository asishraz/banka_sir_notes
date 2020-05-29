#wap to enter an amount in rupees(integer) and print number of 1000,500,100,50,20,10,5 and 1 rupees 
# notes that will be equivalent to the amount entered

amount = int(input("enter the amount in rupees: ")) 
print("the amount is: ", amount)
# for_thousand = 0
# for_fivehundred = 0
# for_hundred = 0
# for_fifty = 0
# for_twenty = 0
# for_ten = 0
# for_five = 0
# for_one = 0
# new_amount = 0

#e.g - 1995



def check_thousand(amount):
    for_thousand = 0
    for_thousand = amount // 1000
    amount = amount - (for_thousand * 1000)
    print("it has " + str(for_thousand) + " thousand")
    if amount >= 500 and amount < 1000:
        check_fivehundred(amount)
    elif amount >= 100 and amount < 500:
        check_hundred(amount)
    elif amount >= 50 and amount < 100:
        check_fifty(amount)
    elif amount >= 20 and amount < 50:
        check_twenty(amount)
    elif amount >=10 and amount < 20:
        check_ten(amount)
    elif amount >=5 and amount < 10:
        check_five(amount)
    elif amount >=1 and amount < 5:
        check_one(amount)
    elif amount == 1000:
        for_thousand = 1


def check_fivehundred(amount):
    for_fivehundred = 0
    for_fivehundred = amount // 500
    amount = amount - (for_fivehundred * 500)
    print("it has " + str(for_fivehundred) + " five-hundred")
    if amount >= 100 and amount < 500:
        check_hundred(amount)
    elif amount >= 50 and amount < 100:
        check_fifty(amount)
    elif amount >= 20 and amount < 50:
        check_twenty(amount)
    elif amount >=10 and amount < 20:
        check_ten(amount)
    elif amount >=5 and amount < 10:
        check_five(amount)
    elif amount >=1 and amount < 5:
        check_one(amount)
    elif amount == 500:
        for_fivehundred = 1

def check_hundred(amount):
    for_hundred = 0
    for_hundred = amount // 100
    amount = amount - (for_hundred * 100)
    print("it has " + str(for_hundred) + " hundred")
    if amount >= 50 and amount < 100:
        check_fifty(amount)
    elif amount >= 20 and amount < 50:
        check_twenty(amount)
    elif amount >=10 and amount < 20:
        check_ten(amount)
    elif amount >=5 and amount < 10:
        check_five(amount)
    elif amount >=1 and amount < 5:
        check_one(amount)
    
    elif amount == 100:
        for_hundred = 1


def check_fifty(amount):
    for_fifty = 0
    for_fifty = amount // 50
    amount = amount - (for_fifty * 50)
    print("it has " + str(for_fifty) + " fifty")
    if amount >= 20 and amount < 50:
        check_twenty(amount)
    elif amount >=10 and amount < 20:
        check_ten(amount)
    elif amount >=5 and amount < 10:
        check_five(amount)
    elif amount >=1 and amount < 5:
        check_one(amount)
    
    elif amount == 50:
        for_fifty = 1

def check_twenty(amount):
    for_twenty = 0
    for_twenty = amount // 20
    amount = amount - (for_twenty * 20)
    print("it has " + str(for_twenty) + " twenty")
    if amount >= 10 and amount < 20:
        check_ten(amount)
    elif amount < 10 and amount >= 5:
        check_five(amount)
    elif amount >=1 and amount < 5:
        check_one(amount)
    elif amount == 20:
        for_twenty = 1 

def check_ten(amount):
    for_ten = 0
    for_ten = amount // 10
    amount = amount - (for_ten * 10)
    print("it has " + str(for_ten) + " ten")
    if amount >= 5 and amount < 10:
        check_five(amount)
    elif amount < 5 and amount >= 1:
        check_one(amount)
    elif amount == 10:
        for_ten = 1

def check_five(amount):
    for_five = 0
    for_five = amount // 5
    amount = amount - (for_five * 5)
    print("it has " + str(for_five) + " five")
    if amount >= 1 and amount < 5:
        check_one(amount)
    elif amount == 5:
        for_five = 1

def check_one(amount):
    for_one = 0
    for_one = amount // 1
    amount = amount - (for_one * 1)
    print("it has " + str(for_one) + " one")
    if amount == 1:
        for_one = 1

var = check_thousand(amount)

# print("it breaks down to " + str(for_thousand) + " thousand and " + str(for_fivehundred) + " five hundred and " + str(for_hundred) + " hundred and " + str(for_fifty) + " fifty and " + str(for_twenty) + " twenty and " + str(for_ten) + " ten and " + str(for_five) + " five and " +str(for_one) + " one")

    





# if amount > 1000 :
#     for_thousand = amount // 1000 #1
#     amount = amount - (for_thousand * 1000) #995
#     if amount < 1000:
#         if amount > 500:
#             for_fivehundred = amount // 500 #1
#             amount = amount - (for_fivehundred * 500) #495
#         elif amount == 500:
#             for_fivehundred = 1
#             if amount < 500:
#                 if amount > 100 and amount < 500:
#                     for_hundred = amount // 100 #4
#                     amount = amount - (for_hundred * 100) #95
#                 elif amount == 100:
#                     for_hundred = 1
#                 if amount < 100:
#                     if amount > 50 and amount < 100:
#                         for_fifty = amount // 50 #1
#                         amount = amount - (for_fifty * 50) #45
#                     elif amount == 50:
#                         for_fifty = 1
#                         if amount < 50:
#                             if amount > 20 and amount < 50:
#                                 for_twenty = amount // 20 #2
#                                 amount = amount - (for_twenty * 20) #5
#                             elif amount == 20:
#                                 for_twenty = 1
#                                 if amount < 20:
#                                     if amount > 10 and amount < 20:
#                                         for_ten = amount // 10 
#                                         amount = amount - (for_ten * 10)
    
#                                     elif amount == 10:
#                                         for_ten = 1
#                                         if amount < 10:
#                                             if amount > 5 and amount < 10:
#                                                 for_five = amount // 5
#                                                 amount = amount - (for_five * 5)

#                                             elif amount == 5:
#                                                 for_five = 1
#                                                 if amount < 5:
#                                                     if amount > 1 and amount < 5:
#                                                         for_one = amount // 1
#                                                         amount = amount - (for_one * 1)
#                                                     elif amount == 1:
#                                                         for_one = 1

            



    
'''elif amount == 1000:
    for_thousand = 1

elif amount < 1000:
    print("in the second loop")
    if amount > 500:
        for_fivehundred = amount // 500 #1
        amount = amount - (for_fivehundred * 500) #495
    elif amount == 500:
        for_fivehundred = 1

    elif amount > 100 and amount < 500:
        for_hundred = amount // 100 #4
        amount = amount - (for_hundred * 100) #95
    
    elif amount == 100:
        for_hundred = 1

    elif amount > 50 and amount < 100:
        for_fifty = amount // 50 #1
        amount = amount - (for_fifty * 50) #45

    elif amount == 50:
        for_fifty = 1
    elif amount > 20 and amount < 50:
        for_twenty = amount // 20 #2
        amount = amount - (for_twenty * 20) #5
    elif amount == 20:
        for_twenty = 1

    elif amount > 10 and amount < 20:
        for_ten = amount // 10 
        amount = amount - (for_ten * 10)
    
    elif amount == 10:
        for_ten = 1

    elif amount > 5 and amount < 10:
        for_five = amount // 5
        amount = amount - (for_five * 5)

    elif amount == 5:
        for_five = 1

    elif amount > 1 and amount < 5:
        for_one = amount // 1
        amount = amount - (for_one * 1)
    elif amount == 1:
        for_one = 1
    
    '''







    