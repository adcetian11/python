a=int(input("Enter any number :"))
rev=0
b=a
while(a>0) :
    temp=a%10
    rev=(rev*10)+temp
    a=a//10
print("reverse no. is : ",rev)
