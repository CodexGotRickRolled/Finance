mode=input("Type 'C' for compound and 'S' for calculating Simple interest")

if mode=='C':
    principal=int(input("Enter principal"))
    rate=int(input("interest rate"))
    time=int(input("Time"))
    a=principal*(1+(rate/100))**time 
    print(a)
if mode=='S':
    principal=int(input("Enter principal"))
    rate=int(input("interest rate"))
    time=int(input("Time"))
    a=principal+((principal*rate*time)/100)
    print(a)