'''implement python inheritance create customer as a parent class display name and phone number 
of customer create derived class deposit from customer class and display the account number and 
balence and also create borrower class from depositor class to display borrower information'''

class customer:
    def __init__(self, name ,phone):
        self.name = name
        self.phone = phone

p1 = customer("Suraj", 901324570)
print("my name is:",p1.name)
print("phone.no.=",p1.phone)

class deposit(customer):
    def __init__(self ,acc_no, balence):
        self.acc_no=acc_no
        self.balence=balence
d1 = deposit(123456,50000)
print("acc. no is :",d1.acc_no)
print("balence:",d1.balence)

class borrow(deposit):
    def __init__(self ,price, date):
        self.price=price
        self.date=date
b1 = borrow(123456,50000)
print("Total price :",b1.price)
print("date:",b1.date)