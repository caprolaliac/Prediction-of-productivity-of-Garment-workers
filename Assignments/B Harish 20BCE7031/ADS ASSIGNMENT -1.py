#!/usr/bin/env python
# coding: utf-8

# In[7]:


name = "harish"
age = "20"

print("Name:", name)
print("Age:", age)


# In[8]:


str = "Datascience is used to extract meaningful insights."
print(str.split())
str = "Datascience\tis\tused\tto\textract\tmeaningful\tinsights"
print(str.split("\t"))
str = "Datascience\nis\nused\nto\nextract\nmeaningful\ninsights"
print(str.split('\n')) 
str = "Datascience is used to extract meaningful insights." 
print(str.split(",")) 


# In[9]:


num_1 = 5
num_2 = 78
product = num_1 * num_2
print("Product of {} and {} is {}".format(num_1,num_2,product))


# In[10]:


num_1 = input("Enter the first number")
num_2 = input("Enter the second number")
product = float(num_1) * float(num_2)
print("Product of {} and {} is {}".format(num_1, num_2,product))


# In[12]:


capital_city = {"karimnagar": "Chennai", "Karnataka": "Bangalore", "Maharasthra": "Mumbai", "Kerala": "Thiruvanantapuram", "Odisha": "Bhubaneswar"}
print(capital_city)


# In[13]:


def createList(r1):
    res = []
    for i in range(r1):
        res.append(i)
    return res
r1 = 1000
print(createList(r1))


# In[14]:


import numpy as np 
dimension = int(input("Enter the dimension of identity matrix:"))
identity_matrix = np.identity(dimension, dtype="int")
print(identity_matrix)


# In[15]:


import numpy as np 
x = np.arange(1, 10).reshape(3,3)
print(x)


# In[16]:


import numpy as np
array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array2 = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
result = array1 + array2
print(result)


# In[17]:


from datetime import datetime, timedelta
start_date = datetime(2023, 2, 1)
end_date = datetime(2023, 3, 1)
dates = []
current_date = start_date
while current_date <= end_date:
    dates.append(current_date.strftime('%Y-%m-%d'))
    current_date += timedelta(days=1)
for date in dates:
    print(date)


# In[18]:


import pandas as pd
dictionary = {'Brand': ['Maruti', 'Renault', 'Hyundai'], 'Sales': [250, 200, 240]}
df = pd.DataFrame(dictionary)
print(df)


# In[ ]:




