
# coding: utf-8

# In[34]:


class Height(object):
    def __init__(self, value, scale):
        if scale.upper() == 'CM':
            self.CM = float(value)
        elif scale.upper() == 'FEET':
            self.CM = value * 30.48
        elif scale.upper() == 'INCH':
            self.CM = value * 30.48 /12
        else: 
            raise StandardError("Fuck the system")
        


# In[37]:


LP = Height(12, 'InCh')
LP.CM


# In[38]:


EP = Height(7, 'Inch')
EP.CM


# In[44]:


WolverineFeet = Height(5, 'Feet') 
WolverineInch = Height(3, 'InCh')
WolverineFeet.CM + WolverineInch.CM

