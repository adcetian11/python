# swapping of two number without using third variable
a=int(input("Enetr num1:"))
b=int(input("Enetr num2:"))
print("before swap:a=",a," b=",b)
a=a+b
b=a-b
a=a-b
print("after swap: a=",a," b=",b)