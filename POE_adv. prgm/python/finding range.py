n=int(input("Enter any number : \n"))
if n<0 :
    print("The entered number is negative.")
elif n>80 :
    print("The entered number is greater than 80.")
elif n>60 and n<80 :
    print(n,"belongs to range [0,70]")
elif n>50 and n<70:
    print(n,"belongs to range[0,60]")
elif n>40 and n<60:
    print(n,"belongs to range[0,50]")
elif n>30 and n<50 :
    print(n,"belongs to range[0,40]")
elif n>20 and n<40 :
    print(n,"belongs to range[0,30]")
elif n>10 and n<30 :
    print(n,"belongs to range[0,20]")
else :
    print(n,"belongs to range[0,10]")
