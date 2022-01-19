#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing important libraries for mysql connector 

import mysql.connector as sql
connection =sql.connect(host="localhost",
                       
user='AB',
password='12345',
database='AB')
print(connection)


# In[2]:


# creating object of cursor that can able to get query 
cursor=connection.cursor()


# In[3]:


cursor.execute('show databases')


# In[4]:


# ittrate throue all the database 
for i in cursor:
    print(i)


# In[5]:


#creating table using sql query via python 
cursor = connection.cursor()

cursor.execute("CREATE TABLE studentinfo (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), subject VARCHAR(255))")


# In[6]:


# insert query using python 
query = "INSERT INTO studentinfo (name, subject) VALUES (%s, %s)"
value = ("John", "Stats")
cursor.execute(query,value)
print("Row inserted",cursor.lastrowid)


# In[7]:


### Insert multiple records in Table
query = "INSERT INTO studentinfo (name, subject) VALUES (%s, %s)"
values = [("Krish", "Stats"),
        ("Joe", "Maths"),
        ("Ankur","Data Science"),
        ("Paul","Data Science"),
        ("Vishal","Maths"),
        ("Krish","Data Science")]
cursor.executemany(query,values)
print("Row inserted",cursor.lastrowid)


# In[8]:


cursor = connection.cursor()
cursor.execute("Select * from studentinfo")


# In[9]:


### Fetch All the Data
cursor.fetchall()


# In[10]:


lst=cursor.fetchall()


# In[11]:


for records in lst:
    print(records)


# In[12]:


cursor.fetchone()


# In[13]:


cursor.execute("Select * from studentinfo where name='Krish'")


# In[14]:


cursor.fetchall()


# In[15]:


cursor.execute("Select subject from studentinfo")
#### Fetch All
cursor.fetchall()


# In[16]:


## Select Distinct Columns
cursor.execute("SELECT DISTINCT subject from studentinfo")
#### Fetch All
cursor.fetchall()


# In[17]:


cursor.execute("SELECT name, subject FROM studentinfo WHERE name = 'Krish' OR subject = 'Data Science'") 
#### Fetch All
cursor.fetchall()


# In[18]:


# drop the data that we had creted 
cursor.execute("DROP TABLE studentinfo") 


# In[ ]:




