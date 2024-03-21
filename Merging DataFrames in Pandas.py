#!/usr/bin/env python
# coding: utf-8

# # Merging Data Frame

# In[1]:


import pandas as pd


# In[9]:


df1 = pd.read_csv(r"C:\Users\ALP_TUF\Desktop\DATA_ANALYST_TUTORIAL\Pandas\LOTR.csv")


# In[10]:


df2 = pd.read_csv(r"C:\Users\ALP_TUF\Desktop\DATA_ANALYST_TUTORIAL\Pandas\LOTR 2.csv")


# In[11]:


df1


# In[8]:


df2


# In[12]:


# left join / merge

df1.merge(df2)


# In[13]:


# inner join
df1.merge(df2, how ='inner', on = 'FellowshipID')


# In[14]:


df1.merge(df2, how ='inner', on = ['FellowshipID','FirstName'])


# In[15]:


# Outer join - alll same values

df1.merge(df2, how = 'outer')


# In[16]:


# left join = take everything from left , and all values from right that matches the left
df1.merge(df2, how = 'left')


# In[17]:



# right join = take everything from right , and all values from left that match

df1.merge(df2, how = 'right')


# In[18]:


# Cross join - each values from the left will be compared to the right


df1.merge(df2, how = 'cross')


# In[22]:


# Join function

df1.join(df2, on = 'FellowshipID', how = 'outer', lsuffix = '_Left', rsuffix ='_Right')


# In[27]:


df4 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), lsuffix='_Left' , rsuffix='_Right', how = 'outer')
df4


# In[31]:


# Concatenate - putting 1 dataframe on top of another

pd.concat([df1,df2])


# In[30]:


pd.concat([df1,df2], join = 'inner')


# In[32]:


pd.concat([df1,df2], join = 'outer')


# In[33]:


pd.concat([df1,df2], join = 'outer', axis = 1)


# In[34]:


# APPEND FUNCTION - deprecated

df1.append(df2)


# In[ ]:




