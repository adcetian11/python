# Find greatest number from 3 numbers using ruby
puts("enter num1:")
num1=gets.chomp.to_i
puts("enter num2:")
num2=gets.chomp.to_i
puts("enter num3:")
num3=gets.chomp.to_i

if(num1>num2) and (num1>num3)
    print("num1:",num1," is greater")
elsif(num2>num3) and (num2>num1)
    print("num2:",num2," is greater")
else
    print("num3:",num3," is greater")
end