# Write a ruby program to find out given year is leap year or not
puts("enter a year:")
y=gets.chomp.to_i
if y % 400 == 0
    puts y,' is leap year'
elsif y % 4==0 && y % 100 != 0 
   puts y,' is leap year'
else  puts y,' is not leap year'
end