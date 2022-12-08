def prime(num):
    n=0
    for i in range(2,n):
        if(num%i==0):
            n=1
        break
    if n==0:
        print("It is prime number")
    else:
        print("It is not a prime number")
prime(2)
