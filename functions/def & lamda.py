"""
Python Programming Questions
(Function, lamda, map, filter, reduce)



1.Question of def(Functions)
Basic
1. Write a function to add two numbers.

def add(n1,n2):
    return n1+n2

print(add(10,50))




2. Write a function to find square of a number.

def sqr(num):
    return num**2

print(sqr(4))




3. Write a function to check even or odd.

def checkeven(num):
    if num%2==0:
        return True
    return False

if checkeven(4):
    print("Even")
else:
    print("Odd")



4. Write a function to find maximum of two numbers.

def checkmax(n1,n2):
    if n1>n2:
        return n1
    return n2
print(checkmax(2,5))



5. Write a function to count vowels in a string.

def countvowel(string):
    vowel = "aeiou"
    count = 0
    for ch in vowel:
        if ch in string:
            count += 1
    return count
print(countvowel("python is the great language"))




Medium
6. Write a function to check palindrome string.

def checkpalin(st):
    if st == st[::-1]:
        return True
    return False
if checkpalin("civic"):
    print("Palindrome")
else:
    print("Not Palindrome")




7. Write a function to find factorial of a number.

def facto(num):
    fact = 1
    for i in range(1,num+1):
        fact  = fact*i
    return fact
print(facto(4))




8. Write a function to return second largest number from a list.

def larg(li):
    li.sort()
    s = li[-2]
    return s
print(larg([5,4,7,8,9,6,3,1,12]))




9. Write a function to remove duplicates from a list.

def rem_dupl(li):
    unq = []
    for el in li:
        if el not in unq:
            unq.append(el)
    return unq
print(rem_dupl([25,12,84,79,55,79,25,63,12,25,]))




10. Write a function to calculate Fibonacci series.




Advanced
11. Write a recursive function for factorial.

def fact(num):
    if num == 1:
        return 1
    else:
        return num* fact(num-1)
print(fact(6))




12. Write a function to check prime number.

def checkprime(num):
    for i in range(2,num//3+1):
        if num%i==0:
            return False
        return True
if checkprime(7):
    print("Prime")
else:
    print("Not Prime")



13. Write a function to find GCD of two numbers.

def gcd(a,b):
    gcd = 1
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
            gcd = i
    return gcd
print(gcd(12,18))




14. Write a function to count frequency of characters in a string.

def frq(string):
    ch = "c"
    if ch in string:
        return string.count(ch)
print(frq("spectacular"))




15. Write a function that accepts any number of arguments and returns sum.

def any_number(*num):
    return sum(num)

print(any_number(10,50,48,15,365,200))




2.Question on lambda
1. Write a lambda function to add two numbers.

add = lambda a,b: a+b

print(add(10,20))




2. Write a lambda function to check even number.

even = lambda num: "Even" if num%2==0 else "Odd"

print(even(21))




3. Write a lambda function to find maximum of two numbers.

maxx = lambda a,b: "a" if a>b else "b"

print(maxx(21,10))




4. Write a lambda to return square of a number.

sqr = lambda num: num**2
print(sqr(4))



5. Write a lambda to return "Pass" if marks > 40 else "Fail".

result = lambda marks: "Pass" if marks>40 else "Fail"

print(result(55))




3.Questions on map()
1. Use map() to square all elements in a list.

li = [x for x in range(1,6)]

square = list(map(lambda num: num**2 , li))
print(sqr)




2. Use map() to convert list of strings into uppercase.

li = ["python"]

string = list(map(lambda lis: lis.upper() , li))
print(string)




3. Use map() to convert list of strings into integers.

li = ["21","30","45","55","14"]

integers = list(map(int , li))
print(integers)



4. Use map() to add elements of two lists.

li1 = [10,20,30,40,50]
li2 = [5,10,15,25,20]
add = list(map(lambda a,b: a+b , li1,li2))
print(add)



5. Use map() to find length of each word in a list.

words = "what is the new program"
w = words.split()

length = list(map(lambda word: len(word) , w))
print(length)




4.Questions on filter()
1. Use filter() to get even numbers from a list.

li = [n for n in range(1,11)]

even = list(filter(lambda num: True if num%2==0 else False , li))
print(even)



2. Use filter() to get odd numbers from a list.

li = [n for n in range(21,31)]

odd = list(filter(lambda num: True if num%2!=0 else False , li))
print(odd)



3. Use filter() to get numbers greater than 50.

greater = list(filter(lambda num: True if num>50 else False , [20,34,51,78,96,84,79,69]))
print(greater)




4. Use filter() to get words starting with vowel.

v = ("a", "e", "i", "o", "u")
words = ["i", "can", "show", "the", "image"]

vowel = list(filter(lambda word: word.startswith(v) , words))
print(vowel)





5.Questions on reduce()
(Use: from functools import reduce)
1. Use reduce() to find sum of elements in a list.

from functools import reduce
li = [x for x in range(1,21+1)]

summ = reduce(lambda a,b: a+b , li)
print(summ)




2. Use reduce() to find product of elements in a list.

from functools import reduce
li = [e for e in range(1,6)]

product = reduce(lambda a,b: a*b , li)
print(product)




3. Use reduce() to find maximum element in a list.

from functools import reduce
li = [26,34,10,20,78,55,46,33]

maximum = reduce(lambda a,b: a if a>b else b , li)
print(maximum)




4. Use reduce() to concatenate a list of strings.

from functools import reduce
st1 ="Python "
st2 = "Programm"

concat = reduce(lambda a,b: a+b , st2,st1)
print(concat)




6.Mixed Practice Questions
1. Use map() and lambda to square all numbers in a list.

sqr = lambda num: num**2
li = [x for x in range(1,11)]

squares = list(map(sqr , li))
print(squares)




2. Use filter() and lambda to get numbers greater than 10.

greater = lambda num: True if num>10 else False

number = list(filter(greater , [20,10,31,12,8,7,19,37,21]))
print(number)




3. Use map() and filter() to square only even numbers.

even = filter(lambda num: True if num%2==0 else False , [x for x in range(1,11)])
sqr = list(map(lambda num: num**2 , even))
print(sqr)




4. Use reduce() to find factorial of a number.

from functools import reduce

fact = reduce(lambda n1,n2: n1*n2 , [x for x in range(1,6)])
print(fact)




5. From a list, remove duplicates and return only even numbers.

li = [36,45,96,21,33,13,20,96,88,95,96,31,33]

dup = filter(lambda num: True if li.count(num)==1 else False , li)
even = list(filter(lambda num: True if num%2==0 else False , dup))
print(even)

