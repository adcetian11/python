num = int(input("Enter a value:"))  
temp = num  
rev = 0  
while(num > 0):  
    dig = num % 10  
    rev = rev * 10 + dig  
    num = num // 10  
if(temp == rev):  
    print("This value is a palindrome number!")  
else:  
    print("This value is not a palindrome number!")  

#another method
value=input("enter your input:")
rev_value=value[::-1]
if value==rev_value:
    print("it is Palindrom!!")
else:
    print("it is not a Palindrom")