#!/usr/bin/env python
# coding: utf-8

# In[16]:


#QUESTION.7.



def prefixToinfix(prefix):
    stack = []
    i=len(prefix) - 1
    while i >=0:
        if not isOperator(prefix[i]):
            stack.append(prefix[i])
            i-=1
        else:
            str = "("+ stack.pop() + prefix[i] + stack.pop() +")"
            stack.append(str)
            i-=1

    return stack.pop()

def isOperator(c):
    if c == "*" or c== "+" or c =="-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False

if __name__=="__main__":
    str = "*-A/BC-/AKL"
    print(prefixToinfix(str))


# In[18]:


#QUESTION.6.
#POSTFIX TO PREFIX


def isOperator(x):

	if x == "+":
		return True

	if x == "-":
		return True

	if x == "/":
		return True

	if x == "*":
		return True

	return False


def postToPre(post_exp):

	s = []

	length = len(post_exp)

	for i in range(length):

		if (isOperator(post_exp[i])):

			op1 = s[-1]
			s.pop()
			op2 = s[-1]
			s.pop()

			temp = post_exp[i] + op2 + op1

			s.append(temp)

		else:

			s.append(post_exp[i])

	
	ans = ""
	for i in s:
		ans += i
	return ans


if __name__ == "__main__":

	post_exp = "AB+CD-"
	
	print("Prefix : ", postToPre(post_exp))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




