A = [1, 2, 3, 4, 5]
result = 1
A.each do |i|
    if i!= 0
        result = result*i
    else
        result
    end
end
puts result