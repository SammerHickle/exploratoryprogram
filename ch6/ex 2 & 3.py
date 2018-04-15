
# coding: utf-8

# In[16]:


def count_spaces(shit):
    page = 0
    for c in shit:
        if c == ' ':
            page = page +1
    return page


# In[27]:


def count_nonspace(shit):
    answer = len(shit) - count_spaces(shit)
    print answer


# In[28]:


count_nonspace('Hello World')

