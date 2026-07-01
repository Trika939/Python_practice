      ##### Python COMPLEX CONDITIONS (AND/OR/NOT) ####

"""

41. Check whether a number is divisible by 5 and 11.

num=int(input("Enter a number : "))
if num%5==0 and num%11==0:
    print("Number is divisible by 5 and 11")
else:
    print("Number is not divisible by 5 and 11")


42. Check if a person is eligible for loan:
● age ≥ 21
● salary ≥ 25,000
● credit score ≥ 700 

age=int(input("Enter your age :"))
salary=int(input("Enter your salary :"))
credit_score=int(input("Enter credit score :"))
if age>=21 and salary>=25000 and credit_score>=700:
    print("This person is eligible for loan")
else:
    print("This person is not eligible for loan") 



----------------------------------------------------------------------------------------
43. Validate login using username AND password.

username=input("Enter username: ")
password=input("Enter password: ")
if username=="admin123" and password=="1234":
    print("Login")
else:
    print("failed Try again")


----------------------------------------------------------------------------------------
44. Check student pass condition:
● All subjects ≥ 40
● Average ≥ 50

all_subjects=int(input("Enter your subject marks : "))
average=int(input("Enter average marks : "))
if all_subjects>=40 and average>=50:
    print("pass")
else:
    print("fail")

    
----------------------------------------------------------------------------------------
45. Check if a number lies between 10 and 100.

num=int(input("Enter a number :"))
if num>=10 and num<=100:
    print("The number lies between 10 and 100.")
else:
    print("The number does not lie between 10 and 100,")



----------------------------------------------------------------------------------------
46. Check exam eligibility:
● attendance ≥ 75% OR
● medical certificate available

attendance=int(input("Enter attendance percentage : "))
medical=input("medical certificate available(yes/no): ")
if attendance>=75 or medical.lower()=="yes":
    print("Eligible for exame")
else:
    print("Not eligible for exam")



----------------------------------------------------------------------------------------
47. Validate a date using conditions.

day=int(input("Enter day : "))
month=int(input("Enter month : "))
years=int(input("Enter years : "))
if day>=1 and day<=31 and month>=1 and month<=31 and years>0:
    print("vaid date")
else:
    print("Invail date")


----------------------------------------------------------------------------------------
48. Check whether an email format is valid.

email=input("Enter your email : ")
if "@" in email and "." in email:
    print("vailed email")
else:
    print("Invailed email")



----------------------------------------------------------------------------------------
49. Determine insurance eligibility using age, health status, and income.

age=int(input("Enter your age : "))
health=input("Enter your health status (good/bed) : ")
income=int(input("Enter your income : "))
if age>=18 and health.lower()=="good" and income>=20000:
    print("eligibility insurance")
else:
    print("Not eligibility insurance")


----------------------------------------------------------------------------------------
50. Check leap year using complete leap year logic.

year=int(input("Enter a year : "))
if (year%400==0) or (year %4==0 and year%100!=0):
               print("Leap year")
else:
    print("Not a leap year")


----------------------------------------------------------------------------------------
"""















