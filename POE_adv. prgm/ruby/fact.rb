puts "Enter the number"
num=gets.chomp.to_i
if num==0
    puts "factorial=1"
else
    fact=1
    for i in 1..num do
        fact = fact * i
        i=i+1
    end
end
print (fact)

