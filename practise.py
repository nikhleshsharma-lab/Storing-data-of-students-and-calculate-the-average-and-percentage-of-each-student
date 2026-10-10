""" n=int(input("enter marks in sub1"))
m=int(input("enter marks in sub2"))
a=int(input("enter marks in sub3"))
t=n+m+a
p=(t/3)
print(f"total is {t} and average is {p}")  """

""" year=int(input())
if(year%4==0 and year%100!=0) or (year%400==0):
    print("leap year")
else:
    print("not a leap year") """

""" a=int(input("enter side1:-"))
b=int(input("enter side2:-"))
c=int(input("enter side3:-"))

if(a+b>c) and (b+c>a) and (c+a>b):
    print("Triangle is valid")
    if(a==b==c):
        print("Equilateral")
    elif(a==b or b==c or c==a):
        print("Isosceles")
    else:
        print("Scalene")        
else:
    print("Triangle is not valid")
 """
""" n=int(input())
fact=1
if(n>=0):
    print(f"{n}!=",end=" ")
    for i in range(n,0,-1):
        fact=fact*i
        print(i,end="*")
    
print(f"={fact}")     """

""" n=int(input("Enter a number:- ")) """
""" sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
print(f"The sum of the digits is {sum}") """

""" k=len(str(n))
l=int(k)
j=0
while n>0:
    n=n%10
    j=j+n**l
    n=n//10
if(j==n):
        print("arm")
else:
        print("not") """


""" m=int(input("enter any number"))
n=m
k=0
while n>0:
    i=n%10
    k=k*10+i
    n=n//10
print(k)
if(k==m):
    print("palindrome")
else:
    print("not palindrome")

k=0
while k=10:
    n=int(input("enter number"))
    k=k+1
    l=0
    if(n>0):
        print("+=",l)
        l=l+1 """
""" n=int(input("enter a number"))
a=0
b=1
while n>0:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    n=n-1  """


n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print(i,end="")
    print()