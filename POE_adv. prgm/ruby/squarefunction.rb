#Write ruby program to find square of any number using the function
def square(a)
    result=a*a
    puts"Square of given number is :#{result}"
end
puts"Enter any number :"
n=gets.chomp.to_i
square(n)