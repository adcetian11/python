# checking pallindrome number
a=int(input("Enter any number :"))
rev=0
b=a
while(a>0) :
    temp=a%10
    rev=(rev*10)+temp
    a=a//10
if (b==rev) :
    print("The given is pallindrome number.")
else :
    print("The given number is not pallindrome.")