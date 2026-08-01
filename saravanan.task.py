#Factorial

n=int(input ("enter the value:"))
fact=1
for i in range(1,n+1):
    fact*=i
    print("Factorial :",fact)

    
    
# for,while   
for i in range(1,11):
    print(i)
    
i=1
while i<=10:
    print(i)
    i+=1


# sum of natural number
    
sum=0
for i in range (1,11):
    i+=sum
    print(i)
    
    
# multiplication
    
n=int(input("enter the value:"))
for i in range (1,n):
    i*=n
    print(i)

    
# fibonacci series

n1=0
n2=1
for i in range(10):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3

    
# palindrome
    
a=int(input("enter the value:"))
b=0
t=a
while t>0:
    d=t%10
    b=b*10+d
    t=t//10
if b==a:
    print(f"{b} palindrome")
else:
    print(f"{b}not palindrome")
    
    

# armstrong

a=int(input("enter the value:"))
b=0
t=a
while t>0:
    d=t%10
    b=b+d**3
    t=t//10
if b==a:
    print(f"{a} is armstrong")
else:
    print(f"{a} is not armstrong")
    

# hcf

a=int(input("enter first number :"))
b=int(input("enter second number :"))
hcf=1
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        hcf=i
print("hcf=",hcf)



#mutiplication print

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("hihello")
    elif i % 3 == 0:
        print("hi")
    elif i % 5 == 0:
        print("hello")
    else:
        print(i)
        

# prime number

n = int(input("Enter number: "))
if n > 1:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} is not prime")
            break
    else:
        print(f"{n} is prime")
else:
    print(f"{n} is not prime")



# prime numbers

count = 0
for num in range(2, 101):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
        count += 1
print(f"\nTotal primes = {count}")  
    

# Divisors

n = int(input("Enter number: "))
print(f"Divisors of {n}: ", end="")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")

        
    
# odd ,even
    
n = int(input("Enter n: "))
sum_even = 0
sum_odd = 0
for i in range(1, n + 1):
    sum_even += 2 * i        
    sum_odd += 2 * i - 1     
print(f"Sum of first {n} even numbers = {sum_even}")
print(f"Sum of first {n} odd numbers = {sum_odd}")



#perfect square

n = int(input("Enter number: "))

if (n ** 0.5) == int(n ** 0.5):
    print(f"{n} is a perfect square")
else:
    print(f"{n} is not a perfect square")







