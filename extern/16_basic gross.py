# python program to take value from user as input basic salary of employee and 
# calculate gross salary
Basic_Salary = int(input("Enter Basic Salary :"))

DA = (Basic_Salary * 40) / 100
HRA = (Basic_Salary * 20) / 100
Gross_Salary = Basic_Salary + DA + HRA

print ("\n\nDearness Allowance 40 % of Basic Salary :" , DA)
print ("House Rent 20 percent of Basic Salary :" , HRA)
print ("Gross Salary :" , Gross_Salary)