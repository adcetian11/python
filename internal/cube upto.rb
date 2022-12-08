puts "Enter no up to which:"
n = gets.chomp.to_i #user input in ruby
i=1
for i in(1..n)
puts(i*i*i) 
i=i+1
end