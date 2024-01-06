import random as r

i=0
def randomnum():
    return r.randint(0,9)
while i<=r.randint(10,100):
    d1=randomnum()
    d2=randomnum()
    d3=randomnum()
    d4=randomnum()

    pin = str(d1)
    pin += str(d2)
    pin += str(d3)
    pin += str(d4)
    i+=1

print('Your Random pin number is:')
print(pin)