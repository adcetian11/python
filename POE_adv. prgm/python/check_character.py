ch=input("Please enter your own chracter")
if((ch>='a' and ch<='z')or(ch>='A' and ch<='Z')):
    print("given chracter",ch, "is an alphabet")
elif(ch>='0' and ch<='9'):
    print("given chracter",ch,"is a digit")
else:
    print("given chracter",ch,"is a special chracter")