puts("Enter first number")
no1= gets.chomp.to_i()
puts("Enter second number")

no2= gets.chomp.to_i()

sum=0
for i in no1..no2  do
	if(i%17==0)
		next
	end
	sum= sum+i
end

puts("Sum of numbers: ",sum)