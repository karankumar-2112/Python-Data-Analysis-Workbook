"""
A.Python IF (Singal Condition)

1. Write a python program to check if a number is positive.

num = int(input("Enter a Number : "))
if num>0:
    print("Positive")



2. Print Eligible to vote if age is 18 or above.

age = int(input("Enter Your Age : "))
if age>=18:
    print("Eligible")



3. Check if a number is divisible by 7.

num = int(input("Enter a Number : "))
if num%7==0:
    print("Yes")



4. Print Pass if marks are greater than 40.

marks = int(input("Enter Your marks : "))
if marks>40:
    print("Pass")




5. Check if a number is greater than 100.

num = int(input("Enter a Number : "))
if num>100:
    print("Yes")




6. Display a message if temperature exceeds 45C.

temp = int(input("What is the Temperature : "))
if temp>45:
    print("High Temperature!")




7. Check if a string lenght is more than 8 characters.

st = 'KaranKumar'
if len(st)>8:
    print("Yes")



8. Print Logged In if password metches admin123.

ps = "admin123"
password = input("Enter the Password : ")
if password==ps:
    print("Logged In")



9. Check if a number is multiple of 10.

n = int(input("Enter a Number : "))
if n%10==0:
    print("Number is multiple of Ten")



10. Print a warning if balance is below minimum limit.

m_limit = 1000
balance = int(input("Show Balance : "))
if balance<m_limit:
    print("Balance can't be less than 1000")




B.Python IF_ELSE (Two Conditions)


11. Check whether a number is Even or Odd.

n = int(input("Enter a Number : "))
if n%2==0:
    print("Even")
else:
    print("Odd")





12. Find the largest of two numbers.

n1 = int(input("Enter First Number : "))
n2 = int(input("Enter second Number : "))
if n1>n2:
    print("Largest Number is",n1)
else:
    print("Largest Number is",n2)




13. Check if a person is eligible for driving license.

age = int(input("Enter Your Age : "))
if age>=18:
    print("Eligible")
else:
    print("Not Eligible")




14. Print Pass or Fail based on marks.

marks = int(input("Enter Your Marks : "))
if marks>=33:
    print("Pass")
else:
    print("Fail")



15. Check whether a number is positive or negative.

num = int(input("Enter a Number : "))
if num>0:
    print("Positive")
else:
    print("Negative")




16. Check whether a character is a vowel or consonant.

ch = input("Enter a character : ").lower()
if ch in 'aeiou':
    print("Vowel")
else:
    print("Consonant")




17. Check if a year is leap or not

year = int(input("Enter the Year : "))
if year%4==0 and year%100!=0 or year%400==0:
    print("Leap Year")
else:
    print("Not Leap Year")




18. Print Vallid Password or Invallid Password.

ps = "karan123"
password = input("Enter The Password : ")
if password==ps:
    print("Vallid")
else:
    print("In Vallid")




19. Determine whether salary is taxable or not.

sal = float(input("Enter Your Salary : "))
if sal>=1275000:
    print("Taxable")
else:
    print("Not Taxable")




20. Check whether a number is greater than 50 or not.

n = int(input("Enter A Number : "))
if n>50:
    print("Yes")
else:
    print("No")




C. Python NASTED IF-ELSE

21. Find the largest of three numbers.

n1 = int(input("Enter The Number : "))
n2 = int(input("Enter The Number : "))
n3 = int(input("Enter The Number : "))
if n1>n2:
    if n1>n3:
        print("Largest Number",n1)
    else:
        print("Largest Number",n3)
else:
    if n2>n3:
        print("Largest Number",n2)
    else:
        print("Largest Number",n3)




22. Check whether a number is posotive, negative, or zero.

num = float("Enter The Nubmer : ")
if num>=0:
    if num==0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")




23. Assign grades:
● A → marks ≥ 90
● B → marks ≥ 75
● C → marks ≥ 60
● Fail → below 60

m = int(input("Enter Your Marks : "))
if m>=90:
    print("A")
else:
    if m>=75:
        print("B")
    else:
        if m>=60:
            print("C")
        else:
            print("Fail")



24. Check whether a triangle is equilateral, isosceles, or scalene.

a = int(input("Enter side length : "))
b = int(input("Enter side length : "))
c = int(input("Enter side length : "))
if a==b:
    if b==c:
        print("Equilateral")
    else:
        print("Isosceles")
else:
    if a==c:
        print("Isosceles")
    else:
        if b==c:
            print("Isosceles")
        else:
            print("Scalene")




25. Check whether a charachter is uppercase, lowercase, digit, special character.

ch = input("Enter a Character : ")
if len(ch)==1:
    if ch>='A' and ch<='Z':
        print("Upper Character")
    else:
        if ch>='a' and ch<='z':
            print("Lower Character")
        else:
            if ch>='0' and ch<='9':
                print("Digit")
            else:
                print("Special Character")
else:
    print("Please Enter Only One Character!")




27. Validate login using username and password.

user = input("Enter Your Username : ")
pas = input("Enter Your Password : ")
if user=="karan":
    if pas=="welcome123":
        print("Login seccesfull")
    else:
        print("Enter Valid Password!")
else:
    print("Enter Valid Username!")




28. Check students result using marks of 3 subjects.

s1 = int(input("Marks of english : "))
s2 = int(input("Marks of maths : "))
s3 = int(input("Marks of science : "))
if s1>=33:
    if s2>=33:
        if s3>=33:
            print("Pass")
        else:
            print("Fail in science")
    else:
        print("Fail in maths")
else:
    print("Fail in english")



29.Find the second largest number among three numbers.

n1 = int(input("Enter First Nubmer : "))
n2 = int(input("Enter Second Nubmer : "))
n3 = int(input("Enter Third Nubmer : "))
if n1<n2:
    if n1>n3:
        print("Second Largest Number n1")
    else:
        print("Second Largest Number n3")
else:
    if n2<n3:
        print("Second Largest Number n2")
    else:
        print("Second Largest Number n3")
        
    

30. Check loan eligibility using age, salary, and credit score.

c1 = int(input("Enter Your Age : "))
c2 = int(input("Enter Your Salary : "))
c3 = int(input("Enter Your Credit Score : "))
if c1>=21 and c1<=65:
    if c2>=15000:
        if c3>=750:
            print("Eligible for loan")
        else:
            print("Credit Score is Below 750")
    else:
        print("Salary is below 15000")
else:
    print("Below The Age")




D. Python ELIF (Multiple Condition)
31. Print day name using day number (1–7).

day = int(input("Enter Day Number : "))
if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thursday")
elif day==5:
    print("Friday")
elif day==6:
    print("Saturday")
elif day==7:
    print("Sunday")




32. Print month name using month number.

mon = int(input("Enter Month Number : "))
if mon==1:
    print("January")
elif mon==2:
    print("February")
elif mon==3:
    print("March")
elif mon==4:
    print("April")
elif mon==5:
    print("May")
elif  mon==6:
    print("June")
elif mon==7:
    print("July")
elif mon==8:
    print("Agust")
elif mon==9:
    print("September")
elif mon==10:
    print("October")
elif mon==11:
    print("November")
elif mon==12:
    print("December")



33. Display grade based on percentage.

per = float(input("Enter Your Percentage : "))
if per>=80:
    print("A")
elif per>=55:
    print("B")
elif per>=50:
    print("C")
elif per>=35:
    print("D")




34. Display bonus percentage based on experience years.
 
exp = float(input("Enter Your Experience : "))
if exp>=10:
    print("15% to 30% Bonus")
elif exp>=4:
    print("5% to 15 Bonus")
elif exp>=0:
    print("1% to 5%")




35. Identify traffic signal meaning.

signal = input("What Signal is: ")
if signal=="red":
    print("Stop Your Vehical")
elif signal=="yellow":
    print("prepare! The signal is about to be red")
elif signal=="green":
    print("You may Go")



36. Categorize temperature as Cold / Warm / Hot.

temp = int(input("Enter The Temperature : "))
if temp>30:
    print("Hot")
elif temp>=20:
    print("Warm")
elif temp<10:
    print("Cold")



37. Categorize employee based on salary range. 

salary = float(input("Enter Your Salary : "))
if salary>=120000:
    print("Senior")
elif salary>=60000:
    print("Manager")
elif salary>=30000:
    print("Junior")
elif salary<30:
    print("Entry Level")




38. Print discount percentage based on purchase amount.

amount = float(input("Enter Purchase Amount : "))
if amount==1000:
    print("75% Discount")
elif amount>=900:
    print("50% Discount")
elif amount>=500:
    print("15% Discount")
elif amount>=200:
    print("5% Discount")




39. Identify number type: single-digit / double-digit / multi-digit.

digit = int(input("Enter Digit : "))
if digit>=100:
    print("multi-digit")
elif digit>=10:
    print("double-digit")
elif digit>=0:
    print("singal-digit")



40. Assign performance rating: Poor / Average / Good / Excellent.

p_rating = float(input("Enter Rating Number : "))
if p_rating>=10:
    print("Excellent")
elif p_rating>=8:
    print("Good")
elif p_rating>=5:
    print("Average")
elif p_rating>=0:
    print("Poor")




E. Python COMPLEX CONDITIONS (AND/OR/NOT)
41. Check whether a number is divisible by 5 and 11.

num = int(input("Enter A Number : "))
if num%5==0 and num%11==0:
    print("Divisible by 5 and 11")
else:
    print("Not divisible by 5 and 11")



42. Check if a person is eligible for loan:
● age ≥ 21
● salary ≥ 25,000
● credit score ≥ 700

age = int(input("Enter Your Age : "))
salary = float(input("Enter Your Salary : "))
cs = int(input("Enter Your Credit Score : "))
if age>=21 and salary>=25000 and cs>=700:
    print("Eligible for loan")
else:
    print("Not eligible for loan")




43. Validate login using username AND password.

user = input("Enter Your Username : ")
pas = input("Enter Your Password : ")
if user=="karan33" and pas=="spy1234":
    print("\n\tLoggin Succesfull!")
else:
    print("\n\tIncorrect Information!")




44. Check student pass condition:
● All subjects ≥ 40
● Average ≥ 50


45. Check if a number lies between 10 and 100.

num = float(input("Enter The Number : "))
if num>=10 and num<=100:
    print("Yes")
else:
    print("No")




46. Check exam eligibility:
● attendance ≥ 75% OR
● medical certificate available

att = int(input("Enter Your Attendance : "))
mc = input("Medical Certificate : ")
if att>=75 or mc=="available":
    print("Eligibile for the Exam")
else:
    print("Not eligible for Exam")




47. Validate a date using conditions.
48. Check whether an email format is valid.

email = input("Enter your Email : ")
if '@' in email and 'gmail' in email and '.com' in email:
    print("Valid email formate")
else:
    print("Not valid formate")




49. Determine insurance eligibility using age, health status, and income.

age = int(input("What is Your Age : "))
hs = input("What your health status is : ")
income = float(input("Enter Your annual income : "))
if age>=18 and hs!='PED' and income>=200000:
    print("Eligible for insurance")
else:
    print("Not eligible for insurance")




50. Check leap year using complete leap year logic.

year = int(input("Enter the Year : "))
if year%4==0 and year%100!=0 or year%400==0:
    print("Leap year")
else:
    print("Leap year")




F. INTERVIEW-LEVEL PYTHON LOGIC QUESTIONS
51. Write a Python program to calculate income tax using slabs.

income = float(input("Enter Your income : "))
it = 0
if income>=2400000:
    it = income*30/100
elif income>=2000001:
    it = income*25/100
elif income>=1600001:
    it = income*20/100
elif income>=1200001:
    it = income*15/100
elif income>=800001:
    it = income*10/100
elif income>=400001:
    it = income*5/100
else:
    print("Nil")
print("Income tax : ",it)





52. Create an ATM withdrawal program with balance checks.

balance = 1000
amount = float(input("Enter the Amount : "))
if amount<=0:
    print("Invalid Amount")
elif amount>balance:
    print("Insufficient Balance")
elif amount<=balance:
    balance = balance-amount
    print("\t\tWithdrawal Succesful : ",amount)
    print("\t\tRemaining Balance : ",balance)




53. Check promotion eligibility using experience and performance.

ex = int(input("Enter Your Experience : "))
per = int(input("Enter the Performance : "))
if ex>=5 and per>=8:
    print("Eligible")
else:
    print("Not eligible")




54. Implement a grading system using nested if–else.

marks = float(input("Enter Your Marks : "))
if marks>=50:
    if marks>=60:
        if marks>=70:
            if marks>=80:
                if marks>=90:
                    print("A+")
                else:
                    print("A")
            else:
                print("B")
        else:
            print("C")
    else:
        print("D")
else:
    print("Fail")




55. Validate strong password using multiple conditions.

pas = input("Enter The Password : ")
lowercase = False
digit = False
schar = False
for ch in pas:
    if ch.islower():
        lowercase = True
    if ch.isdigit():
        digit = True
    if not ch.isalnum():
        schar = True
if len(pas)>=8 and lowercase and digit and schar:
    print("Password Created Succesfully")
else:
    print("Create A Strong Password!")




56. Calculate delivery charges based on location and order amount.

distance = int(input("Enter Your Location Distance : "))
amount = float(input("Enter Your Order-Amount : "))
if distance>=30:
    print(100+amount)
elif distance>=20:
    print(70+amount)
elif distance>=10:
    print(50+amount)
elif distance>=5:
    print("No Delivery Charges :",amount)




57. Determine online exam qualification.

attendance = float(input("Enter Your Attendance : "))
assignment = input("Assignment submitted (Yes/No): ")
if attendance>=75:
    if assignment=="yes":
        print("Qualified for Online Exam")
    else:
        print("Not Qualified for Online Exam")
else:
    print("Not Qualified for Online Exam")




58. Create movie ticket pricing logic based on age & show time.

age = int(input("Enter Your Age : "))
st = input("What Show Time is : ")
price = 0
if 18 <= age <=59 and st=="evening":
    print("Ticket Price : 2000")
elif 18 <= age <=59 and st=="morning":
    print("Ticket Price : 1500")
elif age>=60:
    print("Ticket Price : 120")
elif age<18:
    print("Ticket Price : 100")
else:
    print("Invalid Show Time!")




59. Determine bank account type based on balance.

balance = float(input("Enter Your Balance : "))
if balance>=100000:
    print("VIP Account")
elif balance>=50000 and balance<=99999:
    print("Premium Account")
elif balance>=10000 and balance<=49999:
    print("Saving Account")
elif balance<10000:
    print("Basic Account")




60. Create a menu-driven program using if–elif–else.

print("""\t\t1-Addition
\t\t2-Subtraction
\t\t3-Multiplication
\t\t4-Division
\t\t5-Exit""")
print("\n\t\t----------------")
print("\t\t----------------")
ch = int(input("Enter Your Choice : "))

if ch==1:
    n1 = float(input("\n\t\tEnter First Number : "))
    n2 = float(input("\t\tEnter Second Number : "))
    print("\n\t\tOutcome :",n1+n2)
elif ch==2:
    n1 = float(input("\n\t\tEnter First Number : "))
    n2 = float(input("\t\tEnter Second Number : "))
    print("\n\t\tOutcome :",n1-n2)
elif ch==3:
    n1 = float(input("\n\t\tEnter First Number : "))
    n2 = float(input("\t\tEnter Second Number : "))
    print("\n\t\tOutcome :",n1*n2)
elif ch==4:
    n1 = float(input("\n\t\tEnter First Number : "))
    n2 = float(input("\t\tEnter Second Number : "))
    if n2==0:
        print("Cannot divide by zero!")
    else:
        print("\n\t\tOutcome :",n1/n2)
elif ch==5:
    print("Exiting...")
else:
    print("\n\t\tInvalid Choice!")
    input("\t\tPlease Try Again...")
"""

