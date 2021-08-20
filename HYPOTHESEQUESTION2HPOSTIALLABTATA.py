#!/usr/bin/env python
# coding: utf-8

# In[14]:


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


# In[2]:


LabTAT =pd.read_csv('E:/TUSHAR\ASSINMENT DONE BY TUSHAR/ASSIGNMENT NO 3 (HYPOTHESIS TESTING)/LabTAT.csv')
LabTAT.head()


# In[3]:


LabTAT.describe()


# In[4]:


Laboratory_1=LabTAT['Laboratory 1'].mean()
Laboratory_2=LabTAT['Laboratory 2'].mean()
Laboratory_3=LabTAT['Laboratory 3'].mean()
Laboratory_4=LabTAT['Laboratory 4'].mean()

print('Laboratory 1 Mean = ',Laboratory_1)
print('Laboratory 2 Mean = ',Laboratory_2)
print('Laboratory 3 Mean = ',Laboratory_3)
print('Laboratory 4 Mean = ',Laboratory_4)


# In[8]:


print('Laboratory_1 > Laboratory_2 = ',Laboratory_1 > Laboratory_2)
print('Laboratory_2 > Laboratory_3 = ',Laboratory_2 > Laboratory_3)
print('Laboratory_3 > Laboratory_4 = ',Laboratory_3 > Laboratory_4)
print('Laboratory_4 > Laboratory_1 = ',Laboratory_4 > Laboratory_1)

#The Null and Alternative Hypothesis

#There are no significant differences between the groups' mean Lab values. H0:μ1=μ2=μ3=μ4=μ5

#There is a significant difference between the groups' mean Lab values. Ha:μ1≠μ2≠μ3≠μ4


# In[15]:


sns.distplot(LabTAT['Laboratory 1'])
sns.distplot(LabTAT['Laboratory 2'])
sns.distplot(LabTAT['Laboratory 3'])
sns.distplot(LabTAT['Laboratory 4'])
plt.legend(['Laboratory 1','Laboratory 2','Laboratory 3','Laboratory 4'])


# In[17]:


tStat, pvalue = sp.stats.f_oneway(Lab1,Lab2,Lab3,Lab4)
print("P-Value:{0} T-Statistic:{1}".format(pValue,tStat))


# In[18]:


if pValue < 0.05:
  print('we reject null hypothesis')
else:
  print('we accept null hypothesis')

