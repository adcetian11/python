# 7.Ruby program to print sum of numbers which is not divisible by 17 between the two numbers .
# Input : no1- 1 no2- 20
# Output: sum- 193
sum=0;
for i in 1..20 do
    if(i%17!=0)
        print("\n",i)
        sum=sum+i
    end
end
print("\nsum=",sum)