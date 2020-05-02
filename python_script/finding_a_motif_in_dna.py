#!/usr/bin/env python
# coding: utf-8

# # Finding A Motif in DNA
# ## Problem
# 
# Given two strings **s** and **t**, **t** is a substring of **s** if **t** is contained as a contiguous collection of symbols in **s** (as a result, **t** must be no longer than **s**).
# 
# The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of all occurrences of 'U' in **"AUGCUUCAGAAAGGUCUUACG"** are 2, 5, 6, 15, 17, and 18). The symbol at position **i** of **s** is denoted by s\[i\].
# 
# A substring of **s** can be represented as **s\[j:k\]**, where **j** and **k** represent the starting and ending positions of the substring in **s**; for example, if **s = "AUGCUUCAGAAAGGUCUUACG"**, then **s\[2:5\] = "UGCU"**.
# 
# The location of a substring **s\[j:k\]** is its beginning position **j**; note that **t** will have multiple locations in **s** if it occurs more than once as a substring of **s**.
# 
# > **Given:** Two DNA strings **s** and **t** (each of length at most 1 kbp).
# 
# > **Return:** All locations of **t** as a substring of **s**.

# In[ ]:


def substring_loc(s, t):
    global result
    result = []
    t_len = len(t)
    s_len = len(s)
    for i in range(0, s_len - t_len + 1):
        if s[i:i+t_len] == t:
            result.append(i+1)        
    return result


# In[ ]:


with open("rosalind_subs.txt","r") as motif: #replace filename with your file
    motiff = str()
    for line in motif:
        motiff = motiff + line
    list = motiff.split("\n")

motiff_1 = list[0]
motiff_2 = list[1]
substring_loc(motiff_1,motiff_2)

for i in range(0, len(result)):
    print(result[i], end=" ")

