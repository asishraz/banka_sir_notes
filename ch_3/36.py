'''
n!/(n-r)!r!

print the result of this 
'''


n = int(input("enter the number: "))
r = int(input("enter the number: "))

sub_n = 1
sub_r = 1
diff_n_r = n - r
sub_diff_n_r = 1

for i in range(1,n+1):
    sub_n = sub_n * i


for i in range(1,diff_n_r+1):
    sub_diff_n_r = sub_diff_n_r * i


for i in range(1,r+1):
    sub_r = sub_r * i


final_value = sub_n/ (sub_diff_n_r * sub_r) 

print(final_value)


