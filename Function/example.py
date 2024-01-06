def si_cal(): # def is used to define a function. Here si_cal() is function name
    p = float(input("Enter the principal"))
    r = float(input("Enter the rate of interest"))
    t = float(input("Enter the time"))
    si= (p*r*t) /100
    print(si)

def ci_cal(): # here ci_cal() is a function name
    p = float(input("Enter the principal"))
    r = float(input("Enter the rate of interest"))
    t = float(input("Enter the time"))
    ci= p*(1+r/100)**t
    print(ci)

# si_cal() - calling a function 
# ci_cal() - calling a function