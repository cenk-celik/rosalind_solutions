#!/usr/bin/env python
# coding: utf-8

# # Mortal Fibonacci Rabbits
# ## Problem
# 
# Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation **Fn = Fn − 1 + Fn − 2** and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.
# 
# Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months.
# 
# > **Given:** Positive integers **n ≤ 100** and **m ≤ 20**.
# 
# > **Return:** The total number of pairs of rabbits that will remain after the **n-th** month if all rabbits live for **m** months.

# In[ ]:


n = 89 #replace input                                                                        
m = 16 #replace input                                                                       
bunnies = [1, 1]                                                               
months = 2
count = []                                                                     
while months < n:                                                              
    if months < m:                                                             
        bunnies.append(bunnies[-2] + bunnies[-1])                              
    elif months == m or count == m + 1:                                        
        bunnies.append(bunnies[-2] + bunnies[-1] - 1)                          
    else:                                                                      
        bunnies.append(bunnies[-2] + bunnies[-1] - bunnies[-(                  
            m + 1)])                                                           
    months += 1                                                                
print(bunnies[-1])

