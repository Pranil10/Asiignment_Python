def emical(p,r,n):
    r=r/(12*100)
    n=n*12
    emi=(p*r*((1+r)**n))/((1+r)**n-1)
    return int(emi)

p=int(input("Enter principal/loan amount:-"))
r=float(input("Enter Rate of interest:-"))
n=int(input("Enter the time period in years:-"))
print("Your EMI is ",emical(p,r,n))
