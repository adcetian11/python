bs = float(input("Enter the Basic Salary :"))
if(bs<1500):
    Hra=bs*0.1
    Da=bs*0.9
else:
    Hra=500
    Da=bs*0.98
gs=bs + Hra + Da
print("Gross Salary Rs :",gs)
