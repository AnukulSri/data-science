from example import ci_cal, si_cal

choice = input("What would want to calculate (si/ci)")
if choice =="si":
    si_cal()
elif choice == "ci":
    ci_cal()
else :
    print('invalid choice')
ci_cal