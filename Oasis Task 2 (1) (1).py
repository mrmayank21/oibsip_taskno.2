#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import important libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[3]:


#changing the column names of the given dataset
names = ['States', 'Data', 'Frequency', 'Estimated Unemployment Rate', 'Estimated Employed','Estimated Labour Participation Rate','Region']

#reading the data from the given data set
data=pd.read_csv('Unemployment in India.csv',names=names)
data.head(755)


# In[5]:


data.describe()


# In[6]:


#defining x-axis
x=data['States']
print(x)


# In[7]:


#defining y-axis
y=data['Estimated Unemployment Rate']
print(y)


# In[8]:


data2=data.iloc[:3]
print(data2)


# In[9]:


#visualizing the given dataset using scattered graph
fg=px.scatter(data,x='States',y='Estimated Unemployment Rate',color='States',title='STATE WISE UNEMPLOYMENT RATE',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()


# In[10]:


#visualizing the given dataset using histogram
fg=px.histogram(data,x='States',y='Estimated Unemployment Rate',color='States',title='STATE WISE UNEMPLOYMENT RATE',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()

