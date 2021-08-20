#!/usr/bin/env python
# coding: utf-8

# In[5]:


#import the libraries
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import scipy as sp
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.proportion import proportions_ztest


# In[7]:


Q1_data = pd.read_csv("E:/TUSHAR/ASSINMENT DONE BY TUSHAR/ASSIGNMENT NO 3 (HYPOTHESIS TESTING)/Cutlets.csv")
Q1_data.head()


# In[8]:


Q1_data.describe(include='all')


# In[9]:


Unit_A=Q1_data['Unit A'].mean()
Unit_B=Q1_data['Unit B'].mean()

print('Unit A Mean = ',Unit_A, '\nUnit B Mean = ',Unit_B)
print('Unit A Mean > Unit B Mean = ',Unit_A>Unit_B)


# In[10]:


sns.distplot(Q1_data['Unit A'])
sns.distplot(Q1_data['Unit B'])
plt.legend(['Unit A','Unit B'])


# In[11]:


sns.boxplot(data=[Q1_data['Unit A'],Q1_data['Unit B']],notch=True)
plt.legend(['Unit A','Unit B'])


# In[12]:



alpha=0.05
UnitA=pd.DataFrame(Q1_data['Unit A'])
UnitB=pd.DataFrame(Q1_data['Unit B'])
print(UnitA,UnitB)


# In[13]:


tStat,pValue =sp.stats.ttest_ind(UnitA,UnitB)
print("P-Value:{0} T-Statistic:{1}".format(pValue,tStat))


# In[14]:



if pValue <0.05:
  print('we reject null hypothesis')
else:
  print('we accept null hypothesis')

