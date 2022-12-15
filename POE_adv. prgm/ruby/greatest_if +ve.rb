puts"Enter first number"
a=gets.chomp.to_i
puts"Enter second number"
b=gets.chomp.to_i
puts"Enter third number"
c=gets.chomp.to_i
if a>0 and b>0 and c>0
    puts"Numbers are positive!"
    if a>b and a>c
        puts"#{a} is greatest"
    elsif b>a and b>c
        puts"#{b} is greatest"
    else
        puts"#{c} is greatest"
  end
else
    puts"Numbers are not positive!"
end                         