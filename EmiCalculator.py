amt=int(input("Enter Loan Amount"))
rate=int(input("input Rate of Interest"))
type=input("type 'C' for Compound and 'S' for Simple Interest")
time=int(input("Enter time in months"))
if type=="C":
 total=amt*(1+(rate/100))**(time/12)
 emi=total/time
 print("Total Payment ",total)
 print("Monthly EMI ",emi)
if type=='S':
    total=amt+((amt*rate*time)/100)
    emi=total/time
    print("Total Payment ",total)
    print("Monthly EMI ",emi)