physics=int(input("Enter physics marks: "))
chemistry=int(input("Enter chemistry marks: "))
mathematics=int(input("Enter mathematics marks: "))
biology=int(input("Enter biology marks: "))
computer=int(input("Enter computer marks: "))

percentage=(physics+chemistry+mathematics+biology+computer)/5
print("\n")
if(percentage>=90):
    print("percentage =",percentage)
    print("Grade A")
elif(percentage>=80):
    print("percentage =",percentage)
    print("Grade B")
elif(percentage>=70):
    print("percentage =",percentage)
    print("Grade C")

elif(percentage>=60):
    print("percentage =",percentage)
    print("Grade D")

elif(percentage>=40):
    print("percentage =",percentage)
    print("Grade E")

else:
    print("percentage =",percentage)
    print("Grade F")
