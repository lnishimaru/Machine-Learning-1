#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sklearn


# In[1]:


from sklearn import tree
features=[[140,1],[130,1],[150,0],[170,0]]
labels=[0,0,1,1]
clf=tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)  
print (clf.predict([[150,0]]))


# In[3]:


print (clf.predict([[120,1]]))


# In[ ]:




