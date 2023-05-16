#!/usr/bin/env python
# coding: utf-8

# In[11]:


import os, shutil


# In[12]:


path = r"/Users/KellyLam/Desktop/fe/"


# In[13]:


file_name = os.listdir(path)


# In[15]:


folder_names = ['pdf files', 'image files', 'video files']

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])
for file in file_name:
    if ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)
    elif ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".mov" in file and not os.path.exists(path + "video files/" + file):
        shutil.move(path + file, path + "video files/" + file)

