# This application calculates simple intrest

def s_i(p,n,r):
    i = (p*n*r)/100
    a = p + i
    return i, a

# Take Principal Period and Rate of Intrest as input from user
p = float(input("Please enter Principal in INR : "))
n = float(input("Please enter years : "))
r = float(input("Please enter Rate of Intrest in %p.a."))

# Print the intrest and amout
a, i = s_i(p ,n ,r)
print(f'The Simple Intrest is : {i:.2f} INR')
print(f'The Total amount is : {a:.2f} INR')

