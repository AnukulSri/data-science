from example import si_cal,ci_cal # here we are importing function from previous file named example

choice = input("What would want to calculate (si/ci)") 
if choice =="si": # here we are calling that function
    si_cal()
elif choice == "ci":
    ci_cal()
else :
    print('invalid choice')
ci_cal