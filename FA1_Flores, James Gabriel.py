#!/usr/bin/env python
# coding: utf-8

# In[26]:


kilometer_input = float(input("How many kilometers are there?"))
miles_input = kilometer_input/1.61
print("The distance in miles is",miles_input)


# In[15]:


kilometer_input = float(input("How many kilometers are there?"))
miles_input = kilometer_input/1.61
print("The distance in miles is",miles_input)
Atpm_input = 42//miles_input
print("The average time per mile in minutes is",Atpm_input)
print("and the seconds are"Atpm_input)
sechour_input = 42/60
mph_input = 6.21/sechour_input
print("The average speed in mph is", mph_input)


# In[25]:


kilometer_input = float(input("How many kilometers are there?"))
miles_input = kilometer_input/1.61
print("There are  miles in  kilometers.")
minutes_input = int(input("How many minutes are there?"))
seconds_input = int(input("How many seconds are there?"))
totalseconds = minutes_input*60
avgtime = totalseconds//miles_input
finalmin = avgtime//60
finalsec = (avgtime%60)//1
print(finalmin)


# In[ ]:




