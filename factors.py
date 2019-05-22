p1-check the factors of a number n
def print_factors(n):
    for i in range(1,n+1):
        if(n%i==0):
            print(i)
n=320
print(print_factors(n))


p2-check the number is prime or not
n = 0
if n > 1: 
   for i in range(2, n): 
       if (n % i) == 0: 
           print(n, "is not a prime number") 
           break
   else: 
       print(n, "is a prime number") 
  
else: 
   print(n, "not a prime number") 
   
   
p3-print the primenumbers between two intervals
a=100
b=200
for n in range(a,b+1):
    if n > 1: 
        for i in range(2, n): 
            if (n % i) == 0:
                break
        else:
            print(n)
          
p4-print the prime factors of of n
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
n=320
print(prime_factors(n))


p5-print the no.is perfect no.or not
n=5
sum=0
for i in range(1,n):
    if(n%i==0):
        sum+=i
if(sum==n):
    print(n,"is a perfect number")
else:
    print(n,"is not a perfect number")
    
    
p6-print the no.is perfect square or not
import math

n = int(input())

i = int(math.sqrt(n)) #sqrt function returns float so typecasting to int

if(n == i*i):
  print("perfect Square: %d * %d = %d"%(i,i,n))
else:
  print("Not Perfect Square")
  

p7-count the perfect sqrs between two intervals
def CountSquares(a, b): 
  
    cnt = 0 
    for i in range (a, b + 1): 
        j = 1; 
        while j * j <= i: 
            if j * j == i: 
                 cnt = cnt + 1
            j = j + 1
        i = i + 1
    return cnt
a = 9
b = 25
print ("Count of squares is:", CountSquares(a, b) )



p8-check the given integer is power of two or not
n=int(input())
for i in range(1,n+1):
    if(n==2**i):
        print(n,"is power of two")
        break
else:
    print(n,"is not a power of two")
    
p9-print the perfect square between two intervals
def CountSquares(a, b): 
    
    list=[]
    for i in range (a, b + 1): 
        j = 1; 
        while j * j <= i: 
            if j * j == i: 
                 list.append(i)
            j = j + 1
        i = i + 1
    return list
a = 9
b = 25
print ("Count of squares is:", CountSquares(a, b) )


        
           
