# program to print the table of specific number entered by user
n= int (input("Enter a number:"))
s= 0
a=1
while a<11:
    s = n*a
    print(f'{n} * {a} = {s}')
    a+=1