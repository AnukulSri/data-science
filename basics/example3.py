# calculate the area of triangle 

from re import S
from tkinter import W


def tri():
    a= float(input("Enter base"))
    b = float(input("Enter height"))
    c = float(input("Enter height"))
    s = (a+b+c)/2
    ar = (s*(s-a)*(s-b)*(s-c))**0.5
    print(ar)

def area_of_circle():
    r= float(input("Enter radius of circle"))
    area = 3.14*r**2
    print("The area of circle is ",area)

def area_of_rect():
    l = float(input("Enter length of a rectangle"))
    w = float(input("Enter width of a rectangle"))
    area = l*w
    print(area)

def menu():
    print("1 area of triangle")
    print("2 area of circle")
    print("3 area of rectangle")
    print("4 to quit")

    ch = int(input("Enter your choice"))
    if ch == 1:
         tri()
    elif ch==2:
        area_of_circle()
    elif ch==3:
        area_of_rect()
    elif ch==4:
        print("GoodBye")
    else:
        print("Invalid choice")
        menu()

if __name__=="__main__":
    menu()

