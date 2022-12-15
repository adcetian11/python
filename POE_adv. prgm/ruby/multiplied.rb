puts"Enter first number"
a=gets.chomp.to_i
puts"Enter second number"
b=gets.chomp.to_i

if a%b==0
    puts"#{b} is multiplied by #{a}"
else
    puts"#{b} is not multiplied by #{a}"
end                         