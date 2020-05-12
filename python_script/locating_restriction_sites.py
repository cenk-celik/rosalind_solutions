#!/usr/bin/env python
# coding: utf-8

# # Locating Restriction Sites
# 
# ## The Billion Year War
# 
# ### Problem
# A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC.
# 
# > **Given:** A DNA string of length at most 1 kbp in FASTA format.
# 
# > **Return:** The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

# In[1]:


with open("/Users/cenkcelik/Downloads/rosalind_.txt") as f:
    for line in f:
        if line.startswith(">"):
            dna_str = str()
        else:
            dna_str += (line.strip("\n"))


# In[2]:


def complementary(dna_sequence):
    replace_bases = {"A":"T","T":"A","G":"C","C":"G"}
    return ''.join([replace_bases[base] for base in reversed(dna_sequence)])


# In[7]:


def LocatingRestrictionSites(dna):
    position_length = []
    for i in range(4, 13):
        for j in range(0, len(dna) - i + 1):
            if complementary(dna[j:j+i]) == dna[j:j+i]:
                position_length.append(str(j+1) + ' ' + str(i))
    return position_length


# In[8]:


for fragment in LocatingRestrictionSites(dna_str):
    print(fragment)


# In[ ]:




