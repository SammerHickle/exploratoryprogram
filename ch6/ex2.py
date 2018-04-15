
# coding: utf-8

# In[13]:


def count_spaces(shit):
    page = 0
    for c in shit:
        if c == ' ':
            page = page +1
    return page

