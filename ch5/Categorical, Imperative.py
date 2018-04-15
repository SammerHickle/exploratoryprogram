
# coding: utf-8

# In[5]:


def eqod(num):
    answer = '?'
    if num > 0:
        if (num-1)/2 == num/2:
            answer = 'odd'
        else:
            answer = 'even'
    return answer
            

