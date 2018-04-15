
# coding: utf-8

# In[3]:


def count_nonspaces(shit):
    page = 0
    for c in shit:
        if c == ' ':
            page = page +1
    return len(shit)- page


# In[4]:


count_nonspaces('hello world')

