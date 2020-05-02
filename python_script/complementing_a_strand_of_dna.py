#!/usr/bin/env python
# coding: utf-8

# # Complementing a Strand of DNA
# ## Problem
# 
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# 
# The reverse complement of a DNA string **s** is the string sc formed by reversing the symbols of **s**, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
# 
# > **Given:** A DNA string **s** of length at most 1000 bp.
# 
# > **Return:** The reverse complement **sc** of **s**.

# In[3]:


for N in open("/Users/cenkcelik/Downloads/rosalind_orf.txt","r").read()[::-1]:
    for pair in ["GC","AT"]:
        if N in pair: print("".join(set(N)^set(pair)),end="")


# In[ ]:




