#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv(""C:\Users\91950\Downloads\titanic.csv"")


# In[34]:


df = pd.read_csv("C:/Users/91950/Downloads/titanic.csv")


# In[35]:


sns.countplot(df['survived'])
plt.show()

sns.distplot(df['age'])
plt.show()

sns.boxplot(df['fare'])
plt.show()


# In[36]:


sns.barplot(x='sex', y='survived', data=df)
plt.show()

sns.barplot(x='pclass', y='survived', data=df)
plt.show()

sns.lmplot(x='age', y='fare', data=df)
plt.show()

sns.pairplot(df)
plt.show()

df.describe()


# In[ ]:


df['age'].fillna(df['age'].mean(), inplace=True)
df['fare'].fillna(df['fare'].mean(), inplace=True)


# In[ ]:


df = df[df['age'] < 80]
df = df[df['fare'] < 1000]


# In[ ]:


df['sex'] = df['sex'].astype('category')
df['embarked'] = df['embarked'].astype('category')


# In[ ]:


X = df.drop('survived', axis=1)
y = df['survived']


# In[ ]:


df.dropna(subset=['age', 'embarked'], inplace=True)


# In[ ]:


df['fare'] = np.where((df['fare'] < lower_bound) | (df['fare'] > upper_bound),
                      df['fare'].median(), df['fare'])


# In[ ]:


categorical_cols = ['sex', 'embarked']
df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)


# In[37]:


X = df_encoded.drop('survived', axis=1)
y = df_encoded['survived']

scaler

