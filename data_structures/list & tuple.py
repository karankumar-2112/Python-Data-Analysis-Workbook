"""
Python Programming Question-LIST
Basic Level

1. Write a Python program to create a list of integers and print its elements.

li = [13,24,59,62,37,70,82,92]
print(li)



2. Write a program to find the sum and average of all elements in a list.

li = [15,64,20,38,95,74,66]
print(sum(li))
print(sum(li)/len(li))



3. Write a program to find the largest and smallest element in a list.

li = [15,64,20,38,95,74,66]
print(max(li))
print(min(li))



4. Write a Python program to count the number of elements in a list without using len().

li = [15,64,20,38,95,74,66]
count = 0
for num in li:
    count = count+1
print("Total Numbers of Element :",count)




5. Write a program to reverse a list without using built-in functions.

li = [15,64,20,38,95,74,66]
print(li[-1:-8:-1])



6. Write a program to check if an element exists in a list.

li = [15,64,20,38,95,74,66]
ele = 15
for i in li:
    if ele is i:
        print(i,"Exist")



7. Write a Python program to remove duplicate elements from a list.

li = [15,96,35,74,96,27,84,30,15,35,84]
print(li)
li2 = list(set(li))
print(li2)




8. Write a program to sort a list in ascending and descending order.

li = [26,95,76,38,40,51,13,20,3]
print(li)
li.sort()
print(li)
li.sort(reverse=True)
print(li)



Intermediate Level

9. Write a program to merge two lists and remove duplicates.


li1 = [5,2,8,6,4,9]
li2 = [7,1,4,8,12,2,20]
li1.extend(li2)
print(li1)
li = list(set(li1))
print(li)
# other ways to do this
li1 = [5,2,8,6,4,9]
li2 = [7,1,4,8,12,2,20]

li = list(set(li1+li2))
print(li)

li1 = [5,2,8,6,4,9]
li2 = [7,1,4,8,12,2,20]
for e in li2:
    if e not in li1:
        li1.append(e)
print(li1)




10. Write a program to find common elements between two lists.

li1 = [15,37,64,55,24,78,68]
li2 = [24,78,55,88,15,64,12]
for i in li1:
    if i in li2:
        print(i)



11. Write a program to split a list into even and odd numbers.

li = [1,2,3,4,5,6,7,8,9,10]
even = []
odd = []
for e in li:
    if e%2==0:
        even.append(e)
    else:
        odd.append(e)
print("Even list :",even)
print("Odd list :",odd)



12. Write a program to rotate a list by n positions

li = [0,1,2,3,4,5,6,7,8]
print(li)
posi = int(input("Enter the n position :"))
for i in range(posi):
    li.insert(0,li[len(li)-1])
    li.pop(len(li)-1)
print(li)




13. Write a Python program to find the second largest number in a list. 

li = [26,47,37,65,20,80,70,54,]
li.sort()
second_largest = li[-2]
print("Second Largest Number :",second_largest)




14. Write a program to flatten a nested list. 

nasted= [12,34,60,[74,21,46,],63,[5,9,7],33,16]
flatten = []
for e in nasted:
    if isinstance(e,list):
        flatten.extend(e)
    else:
        flatten.append(e)
print(flatten)




15. Write a program to count frequency of each element in a list. 

li = [62,25,12,10,62,43,59,87,12,43,62,43,]
dic = dict()
for e in li:
    dic.update({e:li.count(e)})
print(dic)




16. Write a program to replace all negative numbers with zero in a list.

li = [-12,63,-84,-96,56,-70,30,10,-28]
for e in range(9):
    if li[e]<0:
        li[e]=0
print(li)




Advanced Level

17. Write a program to remove all occurrences of a given element from a list.

li = [1,2,3,2,4,1,2,2,1,5]
print(li)
unique = []
for e in li:
    if li.count(e)<2:
        unique.append(e)
print(unique)

# by list comprehension
li = [1,2,3,2,4,1,5]
result = [e for e in li if li.count(e)<2]
print(result)




18. Write a program to check if a list is a palindrome. 

li = [1,2,3,5,1]
if li==li[ : :-1]:
    print("Palindrome list")
else:
    print("Not Palindrome list")



19. Write a Python program to find missing numbers in a given list of consecutive integers. 

li = [1,2,3,5,6,8,9]
missing_num = []
for e in range(1,10):   # Hard cord (this will not adjust with any list)
    if e not in li:
        missing_num.append(e)
print("Missing Number :",missing_num)

li = [1,2,3,5,6,8,9]
missing_num = []
for e in range(li[0],li[-1]+1):     # Flaxible cod (this will adjust according to any list)
    if e not in li:
        missing_num.append(e)
print("Missing Number :",missing_num)




20. Write a program to perform element-wise addition of two lists. 

li1 = [10,20,30,40]
li2 = [50,60,70,80]
add = []
for e in range(len(li1)):
    i = li1[e]+li2[e]
    add.append(i)
print("Eliment-wise Addition :",add)




22. Write a program to group elements based on frequency.
li = [3,4,2,6,5,1,3,4,4,5,2,6,1,1]
blk = []
gl = []
for e in li:
    if e not in blk:
        blk.append(e)
        gl.extend([e]*li.count(e))
print(gl)




Python Programming Questions-TUPLE
Basic Level

23. Write a Python program to create a tuple and print its elements.

t = (25,43,68,79,81,20)
print(t)



24. Write a program to find the length of a tuple. 

t = (25,36,94,83,61,20)
print(len(t))




25. Write a program to find the maximum and minimum element in a tuple. 

t = (26,84,93,20,34,21,78,30,54,58)
print(min(t))
print(max(t))




26. Write a program to convert a tuple into a list. 

t = (33,47,21,25,65,69,84,80,)
lis = list(t)
print(lis)




27. Write a program to check if an element exists in a tuple. 

t = (34,59,75,20,62,53,10,19,15)
print(t)
ele = 19
for e in range(len(t)):
    if ele in t:
        print(ele,"Element Exists")
    else:
        print(ele,"Does not Exist")
    break



28. Write a program to count occurrences of an element in a tuple. 

t = (1,2,3,2,4,5,1,2,3)
print(t.count(2))




Intermediate Level
29. Write a program to slice a tuple and display the result.

t = (25,64,16,98,76,25,34,60,21)
print(t[1:7])


30. Write a program to find repeated elements in a tuple.

t = (1,2,3,4,2,5,6,3,4)
rep = []
for e in t:
    if e not in rep and t.count(e)>1:
        rep.append(e)
rep = tuple(rep)
print(rep)




31. Write a program to merge two tuples.

t = (21,34,50,68,71)
t2 = (32,78,81,20,11)
t3 = t+t2
print(t3)



32. Write a program to unpack elements of a tuple into variables.

t = (10,20,30,40)
a,b,c,d = t
print(a)
print(b)
print(c)
print(d)



33. Write a Python program to sort a tuple.

t = (12,54,30,21,18,56,84,72)
t = list(t)
t.sort()
t = tuple(t)
print(t)


34. Write a program to convert a list of tuples into a dictionary.

Advanced Level
35. Write a program to find the index of an element in a tuple.

t = (25,16,14,98,71,30,24,11,62)
ele = 30
for e in t:
    if e==ele:
        index = t.index(e)
        print("Index of",ele,"is",index)



36. Write a program to remove an element from a tuple (without directly modifying it).

t = (25,96,34,87,20,13,54,56,66)
t = list(t)
ele = 13
for e in t:
    if e==ele:
        t.remove(e)
        print(tuple(t))



37. Write a program to find common elements between two tuples.

t = (15,37,89,64,52,48,73,20,17)
t2 = (44,69,73,15,31,37,89,52,48)
common = []
for e in t:
    if e in t2 and e not in common:
        common.append(e)
print(tuple(common))




38. Write a Python program to check if a tuple is a palindrome.

t = (1,2,5,2,1)
if t==t[ : :-1]:
    print("Palindrome tuple")
else:
    print("Not Palindrome tuple")



39. Write a program to find the element with maximum frequency in a tuple.

t = (2,6,4,1,3,5,6,2,4,4,1)
temp = []
maxx = 0
value = 0
for e in t:
    if e not in temp:
        temp.append(e)
        if t.count(e)>maxx:
            maxx = t.count(e)
            value = e
print("The Element",value,"Maximum Frequency",maxx)




40. Write a program to create a nested tuple and access its elements.

t = (49,34,56,(20,16,54),30,87,95)
print(t[3])

# other way to
t = (49,34,56,(20,16,54),30,(27,55,22),87,95)
access = []
for e in t:
    if isinstance(e,tuple):
        access.extend(e)
print(tuple(access))
"""
