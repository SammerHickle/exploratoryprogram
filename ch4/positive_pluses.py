
# coding: utf-8

# In[77]:


def positive(sequence):
    result = 0
    for num in sequence:
        if num > 0:
            result = result + 1
    return result


# In[83]:


positive([2, 7, -3, 0])


# In[81]:


def pluses(sequence):
    result = 0
    for num in sequence:
        if num > 0:
            result = result + num
    return result


# In[82]:


pluses([3,21,-71,0])

