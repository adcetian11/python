num=int(input("Enter the number : "))
for i in range (1,num+1):
    if i%2==0:
        res=i*i
        print(i,end="")
        print ("^2=",res)
