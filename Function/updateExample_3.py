def AOT (a,b,c):
    s = (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5

def AOC (r):
    return 3.14*r**2

def AOR (l,w):
   return l*w

if __name__=='__main__':

    a = 52
    b=45
    c=60
    r=30
    l=10
    w=20

    tri = AOT(a,b,c)
    cir = AOC(r)
    rec = AOR(l,w)

    print(tri)
    print(cir)
    print(rec)
