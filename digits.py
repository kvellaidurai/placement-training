d1-sum of digits
num=int(input())
sum=0
while(num!=0):
    n=num%10
    sum=sum+n
    num=num//10
print(sum)
    
d2-reverse of digits
num=int(input())
reverse=0
while(num>0):
    n=num%10
    reverse=(reverse*10)+n
    num=num//10
print(reverse)
      (OR)
num=input()
n=num[::-1]
print(n)


d3-check palindrome or not
num=input()
n=num[::-1]
if(num==n):
    print("palindrome")
else:
    print("not palinrome")

