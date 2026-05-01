"""
A. Python IF (Single Condition)

1.WAP to check if a number is POSITIVE.

n = int(input("Enter a Number :"))
if n>0:
    print("positive")

2. Print "Eligible to vote" if age is 18 or above.

age = int(input("Enter a Number :"))
if age>=18:
    print("Eligible to vote")


3. Check if a number is divisible by 7.

n = int(input("Enter a Number :"))
if n%7==0:
    print("Divisible by 7")


4. Print "Pass" if marks are greater than 40

marks = int(input("Enter the Marks"))
if marks>40:
    print("Pass")


5. Check if a number is greater than 100.

n = int(input("Enter a Number :"))
if n>100:
    print("number is greater")


6. Display a message if temperature exceeds 45°C

temperature = int(input("Enter the Temperature :"))
if temperature>45:
    print("High temperature")


7. Check if a string length is more than 8 characters.

string = len(input("Enter the characters :"))
if string>8:
    print("length is more than 8")


8. Print "Logged In" if password matches "admin123".

ps = "admin123"
password = input("Enter the password :")
if password==ps:
    print("Logged In")


9. Check if a number is a multiple of 10.

n = int(input("Enter a Number :"))
if n%10==0:
    print("Number is multipe of Ten")


10. Print a warning if balance is below minimum limit.

min_limit = 25000
balance = int(input("Enter the Amount :"))
if balance<min_limit:
              print("!Warning! :","Low Balance Alert")



B.Python IF-ELSE (Two Conditions)

11. Check whether a number is even or odd.

n = int(input("Enter a Number :"))
if n%2==0:
    print("Even Number")
else:
    print("Odd Number")


12. Find the largest of two numbers.


n1 = int(input("Enter a Number :"))
n2 = int(input("Enter a Number :"))
if n1>n2:
    print("n1","Largest Number")
else:
    print("n2","Largest Number")


13. Check whether a person is eligible for driving license.

p_age = int(input("Enter the age :"))
if p_age>=18:
    print("Eligible for license")
else:
    print("Not Eligible for License")


14. Print "Pass" or "Fail" based on marks.

marks = int(input("Enter a Number :"))
if marks>=35:
    print("Pass")
else:
    print("Fail")


15. Check whether a number is positive or negative.

n = int(input("Enter a Number :"))
if n>0:
    print("Positive")
else:
    print("Negative")


16. Check whether a character is a vowel or consonant.

character = input("Enter a character :")
if character=="A":
    print("vowel")
else:
    print("consonant")


18. Print "Valid Password" or "Invalid Password".


ps = input("Enter the Password :")
if ps=="admin123":
    print("Valid Password")
else:
    print("Invalid Password")


19. Determine whether salary is taxable or not.

salary = float(input("Enter the salary :"))
if salary<250000:
    print("Not taxable salary")
else:
    print("Taxable salary")



20. Check whether a number is greater than 50 or not.

num = int(input("Enter a Number :"))
if num>50:
    print("greater than 50")
else:
    print("Not greater than 50")



C. Python NESTED IF-ELSE

21. Find the largest of three numbers.

n1 = 30
n2 = 100
n3 = 20
if n1>n2:
    if n1>n3:
        print("Largest","n1")
    else:
        print("Largest","n3")
else:
    if n2>n3:
        print("Largest","n2")
    else:
        print("Largest","n3")


22. Check whether a number is positive, negative, or zero.

num = 0
if num>0:
    print("Positive")
else:
    if num<0:
        print("Negative")
    else:
        if num==0:
            print("Zero")

         

23. Assign grades:
● A → marks ≥ 90
● B → marks ≥ 75
● C → marks ≥ 60
● Fail → below 60

marks = 78

if marks>90:
    print("A")
else:
    if marks>75:
        print("B")
    else:
        if marks>60:
            print("C")
        else:
            print("Fail")



24. Check whether a triangle is equilateral, isosceles, or scalene.

a = int(input("Enter a number of sides :"))
b = int(input("Enter a number of sides :"))
c = int(input("Enter a number of sides :"))

if a==b:
    if b==c:
        print("equilateral")
    else:
        print("isosceles")
else:
    if a==c:
        print("isosceles")
    else:
        if b==c:
            print("isosceles")
        else:
            print("scalene")



25. Check whether a character is uppercase, lowercase, digit, or special character.

ch = input("Enter a character :")

if ch>="0":
    if ch<="9":
        print("Digit")
    else:
        if ch>="A":
            if ch<="Z":
                print("uppercase")
            else:
                if ch>="a":
                    if ch<="z":
                        print("lowercase")
                    else:
                        print("special character")



26. Calculate electricity bill using slab-wise rates.


27. Validate login using username and password.

user = input("Enter the Username : ")
password = input("Enter the Password : ")

if user=="karan@123":
    if password=="welcome@000":
        print("Login Succeed")
    else:
        print("Invalid information")



28. Check student result using marks of 3 subjects.

hindi = int(input("Enter the marks :"))
english = int(input("Enter the marks :"))
math = int(input("Enter the marks :"))

if hindi>=33:
    if english>=33:
        if math>=33:
            print("pass")
        else:
            print("fail in math")
    else:
        print("fail in english")
else:
    print("fail in hindi")
    print("fail in all subject")



29. Find the second largest number among three numbers.

n1 = int(input("Enter a Number :"))
n2 = int(input("Enter a Number :"))
n3 = int(input("Enter a Number :"))

if n1>n2:
    if n1>n3:
        if n2>n3:
            print("second largest num","n2")
        else:
            print("second largest num","n3")
    else:
        print("second largest num","n1")
else:
    print("second largest num","n3")



30. Check loan eligibility using age, salary, and credit score.

age = int(input("Enter the your age :"))
salary = int(input("Enter your salary :"))
credit_score = int(input("Enter your credit score :"))

if age>=21:
    if salary>=15000:
        if credit_score==700:
            print("approval")
        else:
            print("not approval")
    else:
        print("low salary")
else:
    print("underage")



D. Python ELIF (multiple condition)

31. Print day name using day number (1–7).

day_num = input("Entre  a Day Number :")

if day_num=="1":
    print("Monday")
elif day_num=="2":
    print("Tuseday")
elif day_num=="3":
    print("Wednesday")
elif day_num=="4":
    print("Thursday")
elif day_num=="5":
    print("Friday")
elif day_num=="6":
    print("Saturday")
elif day_num=="7":
    print("Sunday")



32. Print month name using month number.

m_name = input("Enter a Month Number :")

if m_name=="1":
    print("January")
elif m_name=="2":
    print("February")
elif m_name=="3":
    print("March")
elif m_name=="4":
    print("April")
elif m_name=="5":
    print("May")
elif m_name=="6":
    print("June")
elif m_name=="7":
    print("July")
elif m_name=="8":
    print("August")
elif m_name=="9":
    print("September")
elif m_name=="10":
    print("October")
elif m_name=="11":
    print("November")
elif m_name=="12":
    print("December")


33. Display grade based on percentage.

percentage = float(input("Enter the Percentage :"))

if percentage>=90:
    print("A")
elif percentage>=80:
    print("B")
elif percentage>=65:
    print("C")
elif percentage>=50:
    print("D")



34. Display bonus percentage based on experience years.

e_year = float(input("Enter your Experience Year :"))

if e_year>=8:
    print("15%")
elif e_year>=4:
    print("10%")
elif e_year >=1:
    print("5%")



35. Identify traffic signal meaning.

t_signal = "red light"

if t_signal=="red light":
    print("stop the vehicle")
elif t_signal=="yellow light":
    print("wait/prepare to stop")
elif t_signal=="green light":
    print("Go")


36. Categorize temperature as Cold / Warm / Hot.


temp = float(input("Enter the temperature :"))

if temp>=30:
    print("Hot")
elif temp>=21:
    print("Warm")
elif temp<=20:
    print("Cold")



37. Categorize employee based on salary range.

salary = int(input("Enter the salary :"))
if salary>=60000:
    print("Senior")
elif salary>=45000:
    print("Mid-level")
elif salary>=15000:
    print("Junior")



38. Print discount percentage based on purchase amount.

p_amount = float(input("Enter the Amount :"))

if p_amount>=5000:
    print("Discount-20%")
elif p_amount>=2500:
    print("Discount-10%")
elif p_amount>=1100:
    print("Discount-5%")
elif p_amount<=1000:
    print("Discount-0%")



39. Identify number type: single-digit / double-digit / multi-digit.

num = int(input("Enter the Number :"))

if num>=100:
    print("Multi-digit")
elif num>=10:
    print("Double-digit")
elif num>=0:
    print("Single-digit")


40. Assign performance rating: Poor / Average / Good / Excellent.

p_number = float(input("Enter a Number :"))

if p_number>=10:
    print("Excellent")
elif p_number>=7:
    print("Good")
elif p_number>=5:
    print("Average")
elif p_number>=0:
    print("Poor")




E. Pyhton COMPLEX CONDITION (AND/OR/NOT)

41. Check whether a number is divisible by 5 and 11.

num = int(input("Enter the Number :"))
if num%5==0 and num%11==0:
    print("Divisible by 5 and 11")
else:
    print("Not divisible by 5 and 11")



42. Check if a person is eligible for loan:
● age ≥ 21
● salary ≥ 25,000
● credit score ≥ 700

age = 21
salary = 2500
credit_score = 700

if age>=21 or salary>=25000 or credit_score>=700:
    print("Eligible for loan")
else:
    print("Not eligible for loan")



43. Validate login using username AND password.

username = input("Enter the username :")
password = input("Enter the password :")

if username=="karan@22" and password=="key123":
    print("Login successful")
else:
    print("Incorrect information")


44. Check student pass condition:
● All subjects ≥ 40
● Average ≥ 50


45. Check if a number lies between 10 and 100.


num = int(input("Enter the Number between 10-100:"))

if num>=10 and num<=100:
    print("Yes it is")
else:
    print("It is not")



46. Check exam eligibility:
● attendance ≥ 75% OR
● medical certificate available

attendance = input("Enter the Percentage :")
m_certificate = input("Enter the m_certificate :")

if attendance>="75%" or m_certificate=="available":
    print("Eligible for Exam")
else:
    print("Not eligible for Exam")


47. Validate a date using conditions.
48. Check whether an email format is valid.


49. Determine insurance eligibility using age, health status, and income.

age = int(input("Enter the Age :"))
health_status = input("Enter the health status :")
income = float(input("Enter your income :"))

if age>=18 or health_status=="PED" or income>=300000:
    print("Eligible for insurance")
else:
    print("Not eligible for insurance")



F. INTERVIEW-LEVEL PYTHON LOGIC QUESTIONS

51. Write a Python program to calculate income tax using slabs.


income = int(input("Enter your income :"))

if income>=2500000:
    print("30%")
elif income>=2000000:
    print("25%")
elif income>=1600000:
    print("20%")
elif income>=1200000:
    print("15%")
elif income>=800000:
    print("10%")
elif income>=500000:
    print("5%")
elif income<=400000:
    print("Nill")
"""
