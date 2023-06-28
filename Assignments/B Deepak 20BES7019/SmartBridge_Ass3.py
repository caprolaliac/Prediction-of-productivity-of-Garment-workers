#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 2: Load the dataset
df = pd.read_csv("D:\Downloads\Housing.csv")


# In[4]:


# Step 3: Perform visualizations
# Univariate Analysis
sns.histplot(df['price'], kde=True)
plt.show()


# In[5]:



# Bi-Variate Analysis
sns.scatterplot(x='area', y='price', data=df)
plt.show()


# In[6]:


# Multi-Variate Analysis
sns.pairplot(df)
plt.show()


# In[7]:


# Step 4: Perform descriptive statistics
print(df.describe())


# In[8]:


# Step 5: Check for Missing values and deal with them
print(df.isnull().sum())


# In[10]:



# Step 6: Find and replace outliers
# Identify outliers using statistical methods (e.g., Z-score, IQR)
# Replace outliers with appropriate values (e.g., mean, median, trimmed mean)

# Step 7: Check for Categorical columns and perform encoding
categorical_columns = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'furnishingstatus']
df_encoded = pd.get_dummies(df, columns=categorical_columns, drop_first=True)


# In[11]:



# Step 8: Split the data into dependent and independent variables
X = df_encoded.drop('price', axis=1)
y = df_encoded['price']


# In[12]:



# Step 9: Scale the independent variables
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# In[13]:



# Step 10: Split the data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)


# In[14]:



# Step 11: Build the model
model = LinearRegression()


# In[15]:



# Step 12: Train the model
model.fit(X_train, y_train)


# In[16]:



# Step 13: Test the model
y_pred = model.predict(X_test)


# In[18]:



# Step 14: Measure the performance using metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


print('Mean Squared Error:', mse)
print('R-squared:', r2)

