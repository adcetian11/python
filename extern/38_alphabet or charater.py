# python prgm to take value from user as input any character and check whether it is alphabet,digit 
# or special character using case when stm
ch=input("Please enter your own chracter:")
if((ch>='a' and ch<='z')or(ch>='A' and ch<='Z')):
    print("given input",ch, "is an alphabet")
elif(ch>='0' and ch<='9'):
    print("given input",ch,"is a digit")
else:
    print("given input",ch,"is a special chracter")