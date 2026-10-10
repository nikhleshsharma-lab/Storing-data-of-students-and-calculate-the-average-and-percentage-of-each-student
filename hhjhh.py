# Grading System

""" n1 = float(input("Enter Mathematics Score: "))
n2 = float(input("Enter Physics Score: "))
n3 = float(input("Enter Chemistry Score: "))
n4 = float(input("Enter Design Score: "))
n5 = float(input("Enter CS Score: "))

avg = (n1 + n2 + n3 + n4 + n5) / 5

if avg >= 80.1 and avg < 100:
    print(f"{avg}% , Excellent")
elif avg >= 60.1:
    print(f"{avg}% , Good")
elif avg >= 40:
    print(f"{avg}% , Average")
elif avg >= 0 and avg < 40:
    print(f"{avg}% , Needs improvement") """

""" u = float(input("Enter units: "))
c = float(input("Enter cost per unit: "))

print(f"Bill: ₹{u*c}") """

""" #Factorial
n=int(input("Enter the number"))
j=1
for i in range(n,0,-1):
    j*=i
print(f"{n}! = {j}")

#Fibonacci series

num = int(input("Enter number of terms: "))

# First two terms
a = 0
b = 1

print(a, end=" ")
print(b, end=" ")

# Generate remaining terms
for i in range(2, num):
    c = a + b
    print(c, end=" ")
    a = b
    b = c """
""" #Discount Calculator
print("10% Discount if the stuff bought has a value greater than ₹1000")
p=float(input("Enter MRP of the Product"))
q=int(input("Enter quantity of the product"))
print(f"Total Price: ₹{p*q}")
if p*q>=1000:
    print(f"10% Discount, ₹{(p*q)/10}")
    print(f"Amount to be paid after discount: ₹{(p*q)-(p*q)/10}")
else:
    print("No Discount")       """

""" #Tax Calculator
a=int(input("Enter Age: "))
if a<18 and a>0:
    print("No Tax Deduction")
elif a>=18:
    i=float(input("Enter Income PA: "))
    if i>0 and i<=500000:
        print(f"Tax: ₹{i/10}")
    elif i>500000 and i<=1000000:
        print(f"Tax: ₹{i/5}")
    elif i>1000000 and i<=2000000:
        print(f"Tax: ₹{(3*i)/5}")
    else:
        print("Invalid value")
else:
    print("Invalid Age")
 """

""" #Fibonacci Series
l=int(input("Enter limit for the number of times the loop will run: ''"))
a=0
b=1
for i in range(0,l):
    
    print(a,end=" ")
    c=a+b
    a=b
    b=c
     """

""" #Armstrong Numbers
n=int(input("Enter a number: "))
s=str(n)
l=len(s)
j=0
for a in s:
    i=int(a)**l
    j+=i
if n==j:
    print("The Number is Armstrong")
else:
    print("The Number is not Armstrong") """
    

""" 
# Eligibility Checker (Voting & Driving License)

print("=== Check Your Eligibility ===")

age = int(input("Enter your age: "))

if age >= 18:
    print("✓ You are eligible to vote.")
    
elif age < 18:
    print("✗ You are not eligible to vote yet (Must be 18+).") """


""" # Check if a number is prime using a for loop
n = int(input("Enter a number: "))

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not a prime number")
            break
    else:
        print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number") """


rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()  # New line after each row
