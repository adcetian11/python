#Program that reads 5 numbers and counts the +ve no & find avg of those +ve no.
puts"Enter any five numbers : "
a=gets.chomp.to_i
b=gets.chomp.to_i
c=gets.chomp.to_i
d=gets.chomp.to_i
e=gets.chomp.to_i
count=0;
total=0
if a>0
    count+=1
    total +=a
end
if b>0
    count+=1
    total+=b
end
if c>0
    count+=1
    total+=c
end
if d>0
    count+=1
    total+=d
end
if e>0
    count+=1
    total+=e
end
puts"\nThe positive numbers are : #{count}"
avg=total/count
puts"\nThe avg is : #{avg}"
