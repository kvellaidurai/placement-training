d1-sum of digits
num=int(input())
sum=0
while(num!=0):
    n=num%10
    sum=sum+n
    num=num//10
print(sum)
    
