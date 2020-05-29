#input the Basic salary
#and print his take home pay
#take home pay = gross pay - deductions 
#HRA = 20% of (BS + DA)
# DA = 98% of BS
#Grosspay = BS + HRA + DA 
#PF = 8.33% of (BS + DA)
#IT = 20% of Gross pay
# Deductions = PF + IT


basic_sal = int(input("enter the basic salary: "))
DA = (98/100) * basic_sal
bs_and_da = basic_sal + DA
HRA = (20/100) * bs_and_da
gross_pay = basic_sal + HRA + DA
PF = (8.33/100) * bs_and_da
IT = (20/100) * gross_pay
deductions = PF + IT

take_home_pay = gross_pay - deductions

print("after getting the basic salary of " + str(basic_sal) + " , our take home pay is " + str(take_home_pay) + " only")