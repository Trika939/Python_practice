      ### Python NESTED IF–ELSE #####

"""
21.Find the largest of three numbers.

a=4
b=29
c=9
if a>=b and a>=c:
    print("larges a")
else:
    if b>=a and b>=c:
        print("largeat b")   
    else:
        print("largest c")
   
22. Check whether a number is positive, negative, or zero.

num = int(input("Enter A Number : "))
if num>0:
    print("Positive")
else:
    if num<0:
        print("Negative")
    else:
        print("Zero")


23. Assign grades:
 ● A → marks ≥ 90
 ● B → marks ≥ 75
 ● C → marks ≥ 60
 ● Fail → below 60

marks=int(input("Enter your marks: "))
if marks>=90:
    print("A grads")
else:
    if marks>=75:
        print("B gradas")
    else:
        if marks>=60:
            print("c grads")
        else:
            print("fail below 60")


24. Check whether a triangle is equilateral, isosceles, or scalene.

a=4
b=4
c=4
if a==b==c:
    print("Equilateral triangle")
else:    
 if a==b or b==c or a==c: 
  print("isosceles")
 else:
     print("scalene")
    
25. Check whether a character is uppercase, lowercase,
     digit, or special character.

ch = input("Enter a character: ")
if ch>='A' and ch<='Z':
    print("uppercase")
else:
    if ch>='a' and ch<='z':
        print("lowercase")
    else:
        if ch>='0' and ch<='9':
            print("digit")
        else:
            print("special character")

26. Calculate electricity bill using slab-wise rates.

unit=int(input("Enter electricity bill: "))
if unit<=100:
    bill=unit*5
else:
    if unit<=200:
        bill=(100*5)+((unit-100)*7)
    else:
        bill=(100*5)+(100*7)+((unit-200)*10)
        print("Enter bill=$",bill)

        
27.##### Validate login using username and password.         

user_name=input('Enter user ID: ')
password=input('Enter password: '))

if user_name=="admin" :
    if password=="1234" :
        print("Login successful")
    else:
        print("Incorrect password")
else:
    print("Invailed username")



28. Check student result using marks of 3 subjects. 

M=int(input("Enter a subject 1:"))
E=int(input("Enter a subject 2:"))
S=int(input("Enter a subject 3:"))    
if M>=50:
    if E>=50:
        if S>=50:
            total=M+E+S
            percentage=total/3
            print("pass")
            #print("Marks in maths is", M)
            #print("Marks in english is", E)
            #print("Marks in science is", S)
            #print("percentage=",percentage,"%")
        else:
            #print("Marks in maths is", M)
            #print("Marks in english is", E)
            #print("Marks in science is", S)
            print("Fail")
    else:
        print("fail in sub 2")
else:
   print("fail in sub 1")



29. Find the second largest number among three numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if b > c:
        print("Second Largest =", b)
    else:
        if a > c:
            print("Second Largest =", c)
        else:
            print("Second Largest =", a)
else:
    if a > c:
        print("Second Largest =", a)
    else:
        if b > c:
            print("Second Largest =", c)
        else:
            print("Second Largest =", b)        



30. Check loan eligibility using age, salary, and credit score.

age = int(input("Enter age: "))
salary = int(input("Enter salary: "))
credit_score = int(input("Enter credit score: "))

if age >= 21:
    if salary >= 25000:
        if credit_score >= 700:
            print("Loan Approved")
        else:
            print("Loan Rejected - Low Credit Score")
    else:
        print("Loan Rejected - Salary Too Low")
else:
    print("Loan Rejected - Age Less Than 21")


"""
























