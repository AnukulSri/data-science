def si_cal():
    p = float(input("Enter the principal"))
    r = float(input("Enter the rate of interest"))
    t = float(input("Enter the time"))
    si= (p*r*t) /100
    print(si)

def ci_cal():
    p = float(input("Enter the principal"))
    r = float(input("Enter the rate of interest"))
    t = float(input("Enter the time"))
    ci= p*(1+r/100)**t
    print(ci)

# si_cal() 
# ci_cal()