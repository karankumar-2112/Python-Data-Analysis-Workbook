"""
String Programming Questions
# Basic
1. Write a program to count the number of vowels in a string.

st = "AEIOU"
count = 0
for v in st:
    count = count+1
print("Number of vowel :",count)



2. Reverse a string without using built-in functions.

st = "Karan"   
reverse = ""
for ch in st:
    reverse = ch+reverse
print("Reverse:",reverse)



3. Check whether a string is a palindrome.

st = "peep"
if st==st[ : :-1]:
    print("Palindrome String")
else:
    print("Not Palindrome String")



4. Count uppercase and lowercase letters in a string.

st = "KaranKumaR"
countu = 0
countl = 0
for ch in st:
    if ch==ch.upper():
        countu = countu+1
    else:
        countl = countl+1
print("Upper",countu)
print("Lower",countl)



5. Replace all spaces in a string with _.

st = "karan is data analyst"
print(st.replace(" ","_"))




# Intermediate
6. Find the frequency of each character in a string.

st = "karan"
for ch in st:
    print(ch,st.count(ch))

st = "karankumar"
print(st)
visitied = ""
for ch in st:
    if ch not in visitied:
        visitied += ch
        print(ch,st.count(ch))




7. Remove duplicate characters from a string.

st = "karankumar"
unique = ""
for ch in st:
    if ch not in unique:
        unique += ch
print(unique)



8. Find the first non-repeating character in a string.

st = "Programming language"
cha = ""
for ch in st:
    if st.count(ch)==1:
        cha += ch
        print("Non-repeating character :",cha)
        break



9. Check if two strings are anagrams.

st1 = "listen"
st2 = "silent"
if len(st1)==len(st2):
    for ch in st1:
        if st1.count(ch)!=st2.count(ch):
            print("String are not anagram")
            break
    else:
        print("String are anagram")
else:
    print("String are not anagram")



10. Convert "hello world" → "Hello World" (title case without using .title()).

st = "hello world"
conv = []
words = st.split()
for word in words:
    conv.append(word.capitalize())
conv = str(conv)
print(conv)



# Tricky
11. Find the longest word in a sentence.

sentence = "Python is a Programming language"
words = sentence.split()
longest = ""
for word in words:
    if len(word)>len(longest):
        longest = word
print("longest :",longest)




12. Compress a string like "aaabbc" → "a3b2c1".

13. Count words, characters, and digits in a string.

st = "Python 152 7 language for you"
words = len(st.split())
char = len(st)
digit = 0
for d in st:
    if d.isdigit():
        digit += 1
print("words",words)
print("char",char)
print("digit",digit)



14. Rotate a string left by n positions.

st = "SAMSUNG"
st = list(st)
n = int(input("How many rotation :"))
for i in range(n):
    st.insert(len(st),st[0])
    st.pop(0)
st = str(st)
print(st)

#15. Find all substrings of a given string.

Set Programming Questions
Basic

1. Create a set and add elements dynamically.

s = set()
for e in range(21,30):
    s.add(e)
print(s)




2. Find the union and intersection of two sets.

s = {1,2,3,4,5,6,7}
s2 = {8,9,1,2,3,4,7}
print(s.union(s2))          # Symbol |
print(s.intersection(s2))   # Symbol &




3. Remove duplicate elements from a list using a set.

li = [25,47,25,25,23,47,52,11,98]
li = set(li)
print(list(li))




4. Check if an element exists in a set.

s = {26,34,78,51,96,20,12,55}

ele = int(input("Search the Number :"))
if ele in s:
    print("Exists")
else:
    print("Not found")




5. Find the difference between two sets.

s = {6,5,7,2,9,3,4}
s2 = {8,4,5,2,9,6,1}
print(s.difference(s2))    # Symbol -



# Intermediate
6. Find common elements in two lists using sets.

li = [11,12,13,14,15,16]
li2 = [13,14,15,16,17,18]
common_el = set(li).intersection(set(li2))
print(common_el)



7. Check whether one set is a subset of another.

a = {52,84,79,63,10,24,87}
b = {79,10}
print(a)
for el in b:
    if el not in a:
        print("b is not a subset of a")
        break
else:
    print("b is a subset of a")




8. Find symmetric difference of two sets.

s = {6,5,7,2,9,3,4}
s2 = {8,4,5,2,9,6,1}
print(s.symmetric_difference(s2))    # Symbol ^



9. Count unique elements in a list using a set.

li = [54,78,95,21,35,54,78,95,21,35,20]
li = set(li)
print(len(li))




10. Remove all common elements from two sets.

a = {4,7,8,9,6,3,1}
b = {2,6,4,7,8,9,5}
print(a^b)





Tricky
11. Find missing numbers from 1 to n using sets.

s = {1,2,4,6,8,10}
s = list(s)
missing = []
for num in range(s[0],s[-1]+1):
    if num not in s:
        missing.append(num)
print("Missing:",set(missing))




12. Check if two lists have any common elements.

li = [87,96,21,45,35,62,40,88,63]
li2 = [35,62,40,87,21,18,11,94,70]

common_el = set(li) & set(li2)
print(common_el)




13. Convert a set of strings into uppercase.

s = {"karan"}
s = str(s)
print(s.upper())


14. Identify unique vowels in a given string using a set.

string = "python programs are best"
vowel = "aeiou"
unique = set()
for v in vowel:
    if v in string:
        unique.add(v)
print(unique)

15. Find elements that appear only once in a list.




Dictionary Programming Question
Basic
1. Create a dictionary and print all keys and values.

d = {1:32,2:55,3:45,4:20,5:52,6:78}
print(d)




2. Count frequency of each word in a sentence.

s = "i am a programmer and he is a  programmer"
st = s.split()
dic = dict()
for word in st:
    dic.update({word:st.count(word)})
print(dic)




3. Merge two dictionaries.

a = {1:78,2:33,3:15,4:10,5:18,6:96}
b ={7:25,8:66,10:45} 
a.update(b)
print(a)




4. Find the length of a dictionary.

d = {1:32,2:55,3:45,4:20,5:52,6:78}
print(len(d))




5. Check if a key exists in a dictionary.

d = {1:32,2:55,3:45,4:20,5:52,6:78}
print(d)
key = int(input("Enter the key to search :"))
if key in d:
    print("Exists")
else:
    print("Key Not Found")




Intermediate
6. Sort a dictionary by values.

d = {1:32,2:55,3:45,4:20,5:52,6:78}
d = list(d.values())
d.sort(reverse=True)
print(set(d))




7. Find the key with the maximum value.

dic = {1:22,2:45,3:20,4:67,5:14,6:34}
for k,v in dic.items():
    if v== max(dic.values()):
        print(k,v)




8. Remove a key from a dictionary.

d = {1:32,2:55,3:45,4:20,5:52,6:78}
del d[4]
print(d)



9. Convert two lists into a dictionary.

li1 = [1,2,3,4,5,6,7]
li2 = [36,98,74,50,12,20,40]
dic  = dict()
for i in range(len(li1)):
    dic.update({li1[i]:li2[i]})
print(dic)





10. Count character frequency using a dictionary.

st = "Programming"
l = list(st)
frq = dict()
for ch in l:
    frq.update({ch:l.count(ch)})
print(frq)



Tricky
11. Invert a dictionary (swap keys and values).

dic = {"python":1,"mysql":2,"excel":3,"power bi":4}
swap = dict()
for k,v in dic.items():
    swap.update({v:k})
print(swap)




12. Group elements by frequency using a dictionary.

li = [36,45,87,81,20,45,20,45,36]
frq = dict()
for e in li:
    frq.update({e:li.count(e)})
print(frq)




13. Find duplicate values in a dictionary.

dic = {1:48,2:18,3:67,4:25,5:35,6:18,7:25}
li = list(dic.values())
dupt = []
for v in li:
    if li.count(v)>1 and v not in dupt:
        dupt.append(v)
print(dupt)




14. Create a nested dictionary for student records.

student_records = {"student1":{"id":101,"name":"Noby","roll no":25},
       "student2":{"id":102,"name":"Mohan","roll no":26},
       "student3":{"id":103,"name":"Rohan","roll no":27},
       "student4":{"id":104,"name":"Yogesh","roll no":28}}
print(student_records)




15. Flatten a nested dictionary.

nasted = {1:36,2:{3:84,4:69,5:21},6:67,7:74}


Mixed(String + Set + Dictionary)
1. Count unique words in a sentence.

sentence = "python programs are the best programs"
words = sentence.split()
unique = len(set(words))
print(unique)




2. Find common characters between two strings.

st1 = "python"
st2 = "programs"
common_char = set(st1) & set(st2)
print(common_char)




4. Remove duplicate words from a sentence.

sentence = "python programs are not time taking programs"
words = sentence.split()
unique = set(words)
print(unique)
"""
