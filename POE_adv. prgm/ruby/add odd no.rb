puts"Enter any 5 numbers :"
a=gets.chomp.to_i
b=gets.chomp.to_i
c=gets.chomp.to_i
d=gets.chomp.to_i
e=gets.chomp.to_i
add=0
if a%2==1
    add+=a
end
if b%2==1
    add+=b
end
if c%2==1
    add+=c
end
if d%2==1
    add+=d
end
if e%2==1
    add+=e
end

puts"Addition of odd numbers is : #{add}"