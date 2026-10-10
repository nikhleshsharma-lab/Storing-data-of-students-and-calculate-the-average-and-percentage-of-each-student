""" n=float(input())
m=float(input())
k=float(input())
total=n+m+k
avg=total/3
percentage=(total/300)*100
print(f"Total={total}")
print(f"Average={avg}")
print(f"Percentage={percentage:.1f}")
if(n>=40 and m>=40 and k>=40):
    print("Result: pass")
else:
    print("Result: fail")  """


""" total=0
while True:
    n=int(input())
    if(n==0):
        break
    elif(n>0):
        total+=n
    
print(total) """

""" m=int(input())
n=m
l=len(str(n))
k=0
while n>0:
    i=n%10
    k+=i**l
    n=n//10
if(k==m):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number") """
""" 
n=int(input())
for i in range(1,11):
    print(f"{n}*{i}={n*i}") """

m=int(input("enter any number"))
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