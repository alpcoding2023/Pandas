#!/usr/bin/env python
# coding: utf-8

# # Exploratory data analysis (EDA) is used by data scientists to analyze and investigate data sets and summarize their main characteristics, often employing data visualization methods.

# # EDA - 1st look at your data, 
# # Identifying patterns within data
# # Understanding relationship bet features
# # Looking at outlyers that may exists in your data set
#   

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt  # librabry for visualization


# In[2]:


df = pd.read_csv(r"C:\Users\ALP_TUF\Desktop\DATA_ANALYST_TUTORIAL\Pandas\world_population (2).csv")


# In[6]:


# changing float format to 2 decimals if values in scientific notation



pd.set_option('display.float_format', lambda x :'%.2f' % x)


# In[7]:


# first is to have a quick glance using .info & .describe
#
df.info()


# In[8]:


# allow you to get high level overview 
df.describe()


# In[9]:


# check how many values that are missing (null)

df.isnull().sum()


# In[11]:


# check how many unique values each columns has

df.nunique()


# In[15]:


# To see which column has the hightest value we can do either get max, min, or mean 
# Or order values descending by Column
# Top values - .head()


df.sort_values(by="2022 Population", ascending = False).head(10)


# In[16]:


df.sort_values(by="World Population Percentage", ascending = False).head(10)


# In[17]:


# Look at coorelations - usually for numeric values
df.corr()


# In[19]:


# vizualizing correlation using heatmap

sns.heatmap(df.corr(), annot = True)
plt.rcParams['figure.figsize'] = (20, 7)
plt.show()


# In[20]:


# Group columns to look at dataset a little closer

# Group by 'Continent' - to see growth rate by year

df.groupby('Continent').mean()


# In[21]:


# Exploring specific values

df[df['Continent'].str.contains('Oceania')]


# In[22]:


# Order & Sort

df.groupby('Continent').mean().sort_values(by = "2022 Population", ascending = False)


# In[24]:


# Have a quick visualization to see the growth rate 

df2 = df.groupby('Continent').mean().sort_values(by = "2022 Population", ascending = False)

df2.plot()


# In[27]:


# Customize line graph accordingly

# switch Continents to columns and legend become index

df3 = df2.transpose()
df3.plot()


# In[34]:


# Isolate neccasiry value


#df.columns

#Index(['Rank', 'CCA3', 'Country', 'Capital', 'Continent', '2022 Population',
  #     '2020 Population', '2015 Population', '2010 Population',
   #    '2000 Population', '1990 Population', '1980 Population',
   #    '1970 Population', 'Area (km²)', 'Density (per km²)', 'Growth Rate',
    #   'World Population Percentage'],
    #  dtype='object')

df2 = df.groupby('Continent')[['2022 Population',
       '2020 Population', '2015 Population', '2010 Population',
       '2000 Population', '1990 Population', '1980 Population',
       '1970 Population']].mean().sort_values(by = "2022 Population", ascending = False)

#df2 = df.groupby('Continent')[df.columns[5:13]].mean().sort_values(by = "2022 Population", ascending = False)


# In[38]:


#df3 = df2.transpose()
#df3.plot()

# To reverse the plot direction


df2 = df.groupby('Continent')[['1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population']].mean().sort_values(by = "2022 Population", ascending = False)


# In[39]:


df3 = df2.transpose()
df3.plot()


# In[53]:


#Do quick visualization using  Box plot to find outliers 

df.boxplot(figsize =(20,10))


# In[56]:


# Look dataframe by datatype 'number', 'object', 'numeric', 'float'

df.select_dtypes(include='number')


# In[57]:


df.select_dtypes(include='object')


# In[58]:


df.select_dtypes(include='float')


# In[ ]:




