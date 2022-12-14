num=int(input("enter a number:"))
for i in range(2,num):
    if(num%i!=0):
        print("It is prime number")
    break;
else:
    print("It is not a prime number")
