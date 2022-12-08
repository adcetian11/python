unit = int(input("Enter the unit:"))
def electricitybill():
    if (100 > unit):
        amount = unit*2.5
        charge = 20
    elif (300 > unit >= 100):
        amount = unit*3.5
        charge = 50
    elif (500 > unit >= 300):
        amount = unit*5.5
        charge = 70
    elif (700 > unit >= 500):
        amount = unit*7.5
        charge = 100
    elif (unit >= 700):
        amount = unit*10.5
        charge = 150
    print("Electricity Bill =",amount+charge, "Rs")
electricitybill()
