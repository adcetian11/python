class Car:
    def c(self):
        print("Car is a vehicle.")

class Vehicle(Car):
    def v(self):
        print("Vehicle includes car.")

class Asset(Car):
    def a(self):
        print("Car is an asset.")

class Liability(Car):
    def l(self):
        print("Car is a liability.")

obj1 = Vehicle()
obj2 = Asset()
obj3 = Liability()

obj1.c()
obj1.v()

obj2.c()
obj2.a()

obj3.c()
obj3.l()