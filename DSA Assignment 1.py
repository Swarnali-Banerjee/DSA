#!/usr/bin/env python
# coding: utf-8

# In[3]:


#QUESTION.10

str1=input()
str2=input()
def ratation(str1,str2):
    s=len(str1)
    t=len(str2)
    if s!=t:
        return 0
    temp=str1+str1
    if temp.count(str2)>0:
        return 1
    else:
        return 0
if ratation(str1,str2):
    print("rotational")
else:
    print("Non Rotational")


# In[ ]:





# In[1]:


#QUESTION.10

class Empty:
    def __init__(self):
        self.stack=[]
        self.temp=[]
    def stackk(self):
        num=int(input())
        self.temp.append(num)
    def IsEmpty(self):
        if len(self.temp)==0:
            print("Its Empty")
        else:
            print("Not Empty,Length is :",len(self.temp))
    def minimum(self):
        for i in self.temp:
            if i== min(self.temp):
                self.stack.append(i)
                print("The smallest number is",min(self.stack))
a=Empty()
a.stackk()
a.IsEmpty()
a.stackk()
a.stackk()
a.minimum()


# In[2]:


#QUESTION.2.

def reverse():
    item=input().split()
    item2=[]
    for i in item[::-1]:
        item2.append(i)
    print(item2)
reverse()


# In[ ]:




