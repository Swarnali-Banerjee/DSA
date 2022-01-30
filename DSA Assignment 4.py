#!/usr/bin/env python
# coding: utf-8

# In[4]:


#QUESTION.4
# Write a program to print the first non-repeated character from a string.

NO_OF_CHARS = 256

def CharCountArray(string):
	count = [0] * NO_OF_CHARS
	for i in string:
		count[ord(i)]+= 1
	return count

def firstNonRepeating(string):
	count = CharCountArray(string)
	index = -1
	k = 0

	for i in string:
		if count[ord(i)] == 1:
			index = k
			break
		k += 1

	return index

string = "mohitsmohit"
index = firstNonRepeating(string)
if index == 1:
	print("Either all characters are repeating or string is empty")
else:
	print("First non-repeating character is " + string[index])


# In[9]:


#QUESTION.1

# Write a program to find all pairs of an integer array whose sum is equal to a given number.

def getPairsCount(arr, n, sum):

    count = 0 
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1

    return count
arr = [4,8,6,2,4,-1,9]
n = len(arr)
sum = 8
print("Count of pairs is",
    getPairsCount(arr, n, sum))


# In[ ]:




