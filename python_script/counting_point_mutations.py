#!/usr/bin/env python
# coding: utf-8

# # Counting Point Mutations
# ## Problem
# 
# Given two strings **s** and **t** of equal length, the Hamming distance between **s** and **t**, denoted dH(s,t), is the number of corresponding symbols that differ in **s** and **t**.
# 
# > **Given:** Two DNA strings **s** and **t** of equal length (not exceeding 1 kbp).
# 
# > **Return:** The Hamming distance dH(s,t).

# In[1]:


#the function to find out point mutations
def hamming_distance(seq1, seq2):
    """Calculate the Hamming difference between 'seq1' and 'seq2'."""
    return sum(0 if a == b else 1 for (a, b) in zip(seq1, seq2))


# In[ ]:


#open and read the file
with open("rosalind_hamm.txt","r") as fasta: #replace filename your filename
    sequence = str()
    for line in fasta:
        sequence = sequence + line
    list = sequence.split("\n")

sequence_1 = list[0]
sequence_2 = list[1]


# In[ ]:


hamming_distance(sequence_1, sequence_2)

