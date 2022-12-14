# Write a ruby program to take 5 numbers as input add the odd numbers.
puts("enter num1:")
num1=gets.chomp.to_i

puts("enter num2:")
num2=gets.chomp.to_i

puts("enter num3:")
num3=gets.chomp.to_i

puts("enter num4:")
num4=gets.chomp.to_i

puts("enter num5:")
num5=gets.chomp.to_i

L=[num1, num2, num3, num4, num5]

#taking only odd numbers out of them
l = []
for i in L do
    if i%2!= 0
        l.append(i)
    end
end
puts"odd numbers from inputs is:",l
# length=puts "number of positive numbers=",l.length

sum=print "addition is=",l.inject(0){|sum,i| sum + i }







