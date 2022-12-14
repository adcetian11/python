print("Half Pyramid Pattern of Stars (*):")
for i in range(5):
    for j in range(i+1):
        print("* ", end="")
    print()

print("------------------------------------------------------------")

print("Inverted Half Pyramid of Stars (*):")
for i in range(5):
    for j in range(i, 5):
        print("* ", end="")
    print()

print("------------------------------------------------------------")

print("Full Pyramid Pattern of Stars (*): ")
for i in range(5):
    for s in range(-6, -i):
        print(" ", end="")
    for j in range(i+1):
        print("* ", end="")
    print()

print("------------------------------------------------------------")

print("Inverted Full Pyramid of Stars (*): ")
for i in range(5):
    for s in range(i):
        print(" ", end="")
    for j in range(i, 5):
        print("* ", end="")
    print()

print("------------------------------------------------------------")

print("Pattern of Numbers: ")
num = 1
for i in range(5):
    for j in range(i+1):
        print(num, end=" ")
        num = num+1
    print()
print("------------------------------------------------------------")
print("Pattern of Numbers: ")
num = 1
for i in range(5):
    for j in range(i+1):
        print(num, end=" ")
        num = num+1
    num = 1
    print()
print("------------------------------------------------------------")


# "refer this"
# https://codescracker.com/python/program/python-program-print-star-pyramid-patterns.htm#:~:text=To%20print%20pyramid%20pattern%20of%20stars%2C%20numbers%2C%20or,rows%2C%20whereas%20the%20second%20loop%20corresponds%20to%20columns.