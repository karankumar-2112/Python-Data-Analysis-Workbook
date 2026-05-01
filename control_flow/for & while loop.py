"""
FOR Loop - Programming Question
1. Write a program to print numbers from 1 to 100.

for i in range(1,100+1,1):
    print(i)


2. Write a program to print all even numbers between 1 and 50.
for i in range(1,50+1,1):
    if i%2==0:
        print("Even Number :",i)



3. Write a program to print the sum of first n natural numbers.

n = int(input("Enter a Natural Number :"))
s = 0
for i in range(1,n+1):
    s = s+i
print("sum of first natural number :",s)



4. Write a program to print the multiplication table of a given number.

num = int(input("Enter a Number :"))
table = 0
for i in range(1,10+1):
    table = num*i
    print("Table",table)



5. Write a program to print all elements of a list using a for loop.

li = [12,45,96,32,85,75]
for i in li:
    print(i)


6. Write a program to count the number of vowels in a string.

string = "aeiou"
vowel = "aeiou"
count = 0
for i in string:
    if string is vowel:
        print(i)
        count = count+1
print("Number of vowels :",count)



9. Write a program to calculate the factorial of a number using a for loop.

num = int(input("Enter the Nubmer :"))
count = 1
for i in range(1,num+1,1):
    count = count*i
    if count==720:
        print("The Factorial of a num",count)



10. Write a program to print the reverse of a string using a for loop.

string = "ABCD"
reverse_string = ""
for i in string:
    reverse_string = i+reverse_string
print(reverse_string)



WHILE Loop – Programming Questions

11. Write a program to print numbers from 1 to 50 using a while loop.

num = 50
a = 1
while a<=num:
    print(a)
    a = a+1


12. Write a program to print all odd numbers between 1 and 50.

num = 50
a = 1
while a<=num:
    if a%2==1:
        print(a)
    a = a+1


13. Write a program to calculate the sum of digits of a number.

num = 598
a = 1
sum_ = 0
while a<=num:
    rem = num%10
    sum_ = sum_+rem
    num = num//10
print("sum of the digit :",sum_)



14. Write a program to reverse a number using a while loop.

num = 367
a = 1
r_number = 0
while a<=num:
    rem = num%10
    r_number = r_number*10+rem
    num = num//10
print(r_number)



15. Write a program to find the factorial of a number using a while loop.

num = 6
a = 1
fact = 1
while a<=num:
    fact = fact*a
    a = a+1
print(fact)

16. Write a program to keep taking input from the user until the user enters 0.

num = 1
while num!=0:
    num = int(input("Enter your choice :"))
else:
    print("bey")


18. Write a program to check whether a number is a palindrome.

num = 333
num2 = 333
s = 0
a = 1
while a<=num:
    rem = num%10
    s = s*10+rem
    num = num//10
if s==num2:
    print("Palindrome",s)
else:
    print("Not Palindrome")



19. Write a program to print the Fibonacci series up to n terms.
  
n1 = 0
n2 = 1
a = 0
b = 11
while a<=b:
    n3 = n1+n2
    print(n3)
    n1 = n2
    n2 = n3
    a = a+1
"""
