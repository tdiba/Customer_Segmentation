#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_excel(r"C:\Users\USER\Documents\Chat GPT Projects\RAW DATA\Segmentation\customer_data.xlsx")


# In[3]:


df.head()


# In[5]:


# Age Group and Spending Score Range
df['Age Group'] = pd.cut(df['Age'], bins=[17, 30, 45, 60, 100], labels=['18-30', '31-45', '46-60', '60+'])
df['Spending Score Range'] = pd.cut(df['Spending Score (1-100)'], bins=[0, 25, 50, 75, 100], labels=['Low (1-25)', 'Medium (26-50)', 'High (51-75)', 'Very High (76-100)'])


# In[6]:


df['Age Group']


# In[7]:


# Work Experience Range and Family Size Group
df['Work Experience Range'] = pd.cut(df['Work Experience'], bins=[-1, 10, 20, 40], labels=['0-10 years', '11-20 years', '20+ years'])
df['Family Size Group'] = pd.cut(df['Family Size'], bins=[0, 1, 2, 5], labels=['Single', 'Couple', 'Large Family'], right=False)


# In[13]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[16]:


# Data for Stacked Bar Chart (Age Group and Spending Score Range)
age_spending_data = df.groupby(['Age Group', 'Spending Score Range']).size().unstack(fill_value=0)

# Plotting
plt.figure(figsize=(18, 7))
age_spending_data.plot(kind='bar', stacked=True, ax=plt.gca())

# Adding labels and title
plt.xlabel('Age Group')
plt.ylabel('Number of People')
plt.title('Spending Score by Age Group')

# Adding a legend
plt.legend(title='Spending Score Range')

# Show the plot
plt.show()


# In[17]:


# Stacked Bar Chart
plt.subplot(1, 2, 1)
age_spending_data.plot(kind='bar', stacked=True, ax=plt.gca())
plt.title('Customer Distribution by Age Group and Spending Score Range')
plt.ylabel('Number of Customers')
plt.xlabel('Age Group')


# In[18]:


# Box Plot
plt.subplot(1, 2, 2)
sns.boxplot(x='Age Group', y='Annual Income ($)', data=df)
plt.title('Annual Income Distribution by Age Group')
plt.ylabel('Annual Income ($)')
plt.xlabel('Age Group')

plt.tight_layout()
plt.show()


# In[ ]:




