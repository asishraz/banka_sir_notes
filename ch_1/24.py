#given 1sq + 2sq + 3sq + 4sq + ... + Nsq = (N(N+1)(2N+1))/6
#print the result of following series: 
#(8sq + 9sq + 10sq + ... + 30sq ) + (82sq + 89sq + 90sq + ... + 100sq)  + (27sq + 28sq + 29sq + ... + 41sq)

N1 = 30
N2 = 100
N3 = 41

N1_val = ((N1+1)*((2*N1)+1))/6
N2_val = ((N2+1)*((2*N2)+1))/6
N3_val = ((N3+1)*((2*N3)+1))/6

print(N1_val + N2_val + N3_val)