def simple_interest(p,r,t): # passing parameter to a function, now it will return the output
    return (p*r*t)/100 # returning a data by using return keyword

def compound_interest(p:int , r: int, t:int): # we can define which type of data a variable can hold
    return p*(1+r/100)**t

if __name__=='__main__': # creating a function main in which we call both the function
    p= 10000
    r=5
    t=3
    si =simple_interest(p,r,t) # calling function in a variable
    ci = compound_interest(p,r,t) # calling a function a variable

    print(f'simple interest is {si}')
    print(f'compound interest is {ci}')

