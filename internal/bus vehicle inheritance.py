class Vehicle():
    def description(self):
        print("i am vehicle")
class Car(Vehicle):
    def description(self):
        print("i am car")
class Bus():
    def description(self):
        print("i am Bus")
class Truck():
    def description(self):
        print("i am Truck")
v=Vehicle()
c=Car()
b=Bus()
t=Truck()
v.description()
c.description()
b.description()
t.description()