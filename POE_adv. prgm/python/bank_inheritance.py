class customer:
     def p(self):
        print("We have entered in Customer class")
        a=input('Enter your name: ')
        b=input('Enter your your phone number: ')
        print(" Name  of the customer: "+a)
        print(" Phone number of the customer: "+b)


class depositer(customer):
     def q(self):
        print(" \n We have entered in Depositer class")
        c=input('Enter your account number: ')    
        d=input('Enter your Account balance: ')
        print(" Account number of the customer: "+c)
        print(" Account balance of the customer: "+d)

class borrower(depositer):
    def m(self):
        print("\n We have entered in Borrower class")
        e=input('Enter IFSC CODE: ')
        f=input('Enter your Tansaction id: ')
        print(" IFSC CODE of the customer: "+e)
        print(" Tansaction Id of the customer: "+f)

z=borrower()
z.p()
z.q()
z.m()
