from re import S
from tkinter import W


def tri(): # creating a function
    a= float(input("Enter base"))
    b = float(input("Enter height"))
    c = float(input("Enter height"))
    s = (a+b+c)/2
    ar = (s*(s-a)*(s-b)*(s-c))**0.5
    print(ar)

def area_of_circle(): # creating a function
    r= float(input("Enter radius of circle"))
    area = 3.14*r**2
    print("The area of circle is ",area)

def area_of_rect(): # creating a function
    l = float(input("Enter length of a rectangle"))
    w = float(input("Enter width of a rectangle"))
    area = l*w
    print(area)

def menu(): # creating a function
    print("1 area of triangle")
    print("2 area of circle")
    print("3 area of rectangle")
    print("4 to quit")

    ch = int(input("Enter your choice"))
    if ch == 1:
         tri() # calling a function on the basis of choice
    elif ch==2:
        area_of_circle() # calling a function on the basis of choice
    elif ch==3:
        area_of_rect() # calling a function on the basis of choice
    elif ch==4:
        print("GoodBye") 
    else:
        print("Invalid choice")
        menu() # calling a function main again if user input wrong choice among the given choice

if __name__=="__main__":
    menu()