# 2.Write a ruby program that reads 5 numbers and counts the positive numbers and find the average 
# of those positive number
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

#taking only positive numbers out of them
l = []
for i in L do
    if i % 10 == i
        l.append(i)
    end
end
puts"Positive numbers from the inputs are",l
length=puts "count=",l.length

sum=print "addition is=",l.inject(0){|sum,i| sum + i }

print "average is=",l.inject{ |sum, i| sum + i }.to_f / l.size








