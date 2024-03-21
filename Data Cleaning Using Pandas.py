#!/usr/bin/env python
# coding: utf-8

# In[75]:


import pandas as pd


# In[76]:


df = pd.read_excel(r"C:\Users\ALP_TUF\Desktop\DATA_ANALYST_TUTORIAL\Pandas\Customer Call List.xlsx")


# In[12]:


# Using lstrip & rstrip
#df['Last_Name'] = df['Last_Name'].str.lstrip('...')


# In[15]:


#df['Last_Name'] = df['Last_Name'].str.lstrip('/')
#df['Last_Name'] = df['Last_Name'].str.rstrip('_')


# In[77]:


df


# In[79]:


df.drop_duplicates()
df.drop(columns='Not_Useful_Column')


# In[81]:


df['Last_Name'] = df['Last_Name'].str.strip('123/._')


# In[97]:


#Working with phone numbers
# 1st to strip all unnecessary characters - replace [^a-zA-Z0-9] 
# Convert column in string using either for loop or Lambda
# Format it to 123-545-5421	 (x: x[0:3]+'-'+x[3:6]+'-'x[6:10])
# Replace other characters as nan-- Na-- with space

df['Phone_Number'] = df['Phone_Number'].str.replace('[^a-zA-Z0-9]','')

df['Phone_Number'] = df['Phone_Number'].apply(lambda x: str(x))

df['Phone_Number'] = df['Phone_Number'].apply(lambda x: x[0:3] + '-'+ x[3:6] + '-' + x[6:10] )

df['Phone_Number'] = df['Phone_Number'].str.replace('nan--','')
df['Phone_Number'] = df['Phone_Number'].str.replace('Na--','')
df['Phone_Number'] = df['Phone_Number'].str.replace('--','')


# In[108]:


# Address
#1st check the address how long it can be expanded
# Then split address & turn expand to True
# Assign names to splitted values to be appended - Street_Address, City, State or Zip Code

#df['Address'].str.split(',',2, expand = True)

df[["Street_Address", "City", "Zip_Code"]] = df['Address'].str.split(',',2, expand = True)


# In[113]:


df['Paying Customer'] = df['Paying Customer'].str.replace('Yes','Y')
df['Paying Customer'] = df['Paying Customer'].str.replace('No','N')


# In[114]:


df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes','Y')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No','N')


# In[117]:


df = df.replace('N/a','')


# In[119]:


df = df.fillna('')


# In[121]:


df


# In[122]:


df = pd.read_excel(r"C:\Users\ALP_TUF\Desktop\DATA_ANALYST_TUTORIAL\Pandas\Customer Call List.xlsx")


# In[125]:


df = df.drop(columns = 'Not_Useful_Column')


# In[127]:


df['Last_Name'] = df['Last_Name'].str.strip('123/._')

df['Phone_Number'] = df['Phone_Number'].str.replace('[^a-zA-Z0-9]','')

df['Phone_Number'] = df['Phone_Number'].apply(lambda x: str(x))

df['Phone_Number'] = df['Phone_Number'].apply(lambda x: x[0:3] + '-'+ x[3:6] + '-' + x[6:10] )

df['Phone_Number'] = df['Phone_Number'].str.replace('nan--','')
df['Phone_Number'] = df['Phone_Number'].str.replace('Na--','')
df['Phone_Number'] = df['Phone_Number'].str.replace('--','')


df[["Street_Address", "City", "Zip_Code"]] = df['Address'].str.split(',',2, expand = True)

df['Paying Customer'] = df['Paying Customer'].str.replace('Yes','Y')
df['Paying Customer'] = df['Paying Customer'].str.replace('No','N')

df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes','Y')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No','N')

df = df.fillna('')

df

#df = df.replace('N/a','')


# In[128]:


# FILTERING DO NOT CALL Customers

for x in df.index :
    if df.loc[x, "Do_Not_Contact"] == 'Y' :
        df.drop(x, inplace = True)
df


# In[130]:


# Filter Phone numbers that are blank

for x in df.index :
    if df.loc[x, "Phone_Number"] == '' :
        df.drop(x, inplace = True)
df

#Another way of dropping null values for a specific column

#  df.dropna(subset = "Phone_Number", inplace = True)


# In[131]:


# reset index

df.reset_index(drop = True)


# In[ ]:




