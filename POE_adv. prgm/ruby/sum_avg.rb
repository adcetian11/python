puts("Enter the size of array")
n=gets.to_f
k=n-1
arr=Array.new(k)
puts("Enter the numbers ")
countn=0
count=0
for i in (0..k) do
    arr[i]=gets.to_f
end
sum=0
sumn=0
for i in arr do
    if i>0
        sum=sum+i 
        count=count+1
    else 
        sumn=sumn+i
        countn=countn+1
    end
end
average=sum /count
avgn=sumn/countn
puts("the sum of positive number is #{sum} \n the average of positive number is #{average} \n the average of Negavtive number is #{avgn}")