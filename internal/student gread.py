phy=int(input("Enter the Marks in Physics:\n"))
chem=int(input("Enter the Marks in Chemistry:\n"))
bio=int(input("Enter the Marks in Biology:\n"))
math=int(input("Enter the Marks in Mathematics:\n"))
IT=int(input("Enter the Marks in IT:\n"))
per=(phy+chem+bio+math+IT)*100/500
print(per)
if(per>=90):
    print("Grade A")
elif(90>per>=80):
    print("Grade B")
elif(80>per>=70):
    print("Grade C")
elif(70>per>=60):
    print("Grade D")
elif(60>per>=40):
    print("Grade E")
else:
    print("Fail!!")