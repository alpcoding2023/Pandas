#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[38]:


df = pd.read_csv(r"C:\Users\ALP_TUF\Desktop\DATA_ANALYST_TUTORIAL\Pandas\Ice Cream Ratings.csv")


# In[3]:


df


# In[39]:


df = df.set_index('Date')


# In[5]:


df


# In[55]:


# check plot style theme

print(plt.style.available)
plt.style.use('fivethirtyeight')


# In[56]:


df.plot()


# In[36]:





# In[7]:


df.plot(kind = 'line')


# In[9]:


# Breaking by column
df.plot(kind = 'line', subplots = True)


# In[10]:


df.plot(kind = 'line', title =  "ICE CREAM RATINGS")


# In[13]:


df.plot(kind = 'line', title =  'ICE CREAM RATINGS', xlabel = 'Daily Ratings', ylabel = 'Scores')


# In[15]:


# BAR PLOT

df.plot(kind = 'bar')


# In[16]:


# Stacked BAR PLOT

df.plot(kind = 'bar', stacked = True)


# In[18]:


#Specify which ones to plot

df['Flavor Rating'].plot(kind = 'bar', stacked = True, title = " Flavor Rating ")


# In[21]:


# Horizontal bar

df.plot.barh(stacked = True, title = " Flavor Rating ")


# In[22]:


# scatter plot

df.plot.scatter(x = 'Texture Rating', y = 'Overall Rating')


# In[25]:


# Change size, & color
df.plot.scatter(x = 'Texture Rating', y = 'Overall Rating', s = 500, color = 'red')


# In[26]:


# histogram 

df.plot.hist()


# In[30]:


#= specify bins
df.plot.hist(bins = 6)


# In[31]:


# BOX PLOT

df.boxplot()


# In[32]:


# Area plot

df.plot.area()


# In[33]:


# CHANGE SIZE

df.plot.area(figsize = (10, 5))


# In[34]:


# PIE CHART

df.plot.pie(y = 'Flavor Rating')


# In[35]:



df.plot.pie(y = 'Flavor Rating', figsize = (10, 6))


# In[ ]:




