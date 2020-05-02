#!/usr/bin/env python
# coding: utf-8

# # Overlap Graphs
# ## Problem
# 
# A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.
# 
# A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail **v** and head **w** is represented by **(v,w)** (but not by **(w,v)**). A directed loop is a directed edge of the form **(v,v)**.
# 
# For a collection of strings and a positive integer **k**, the overlap graph for the strings is a directed graph O_k in which each string is represented by a node, and string **s** is connected to string **t** with a directed edge when there is a length **k** suffix of **s** that matches a length **k** prefix of **t**, as long as **s ≠ t**; we demand **s ≠ t** to prevent directed loops in the overlap graph (although directed cycles may be present).
# 
# > **Given:** A collection of DNA strings in FASTA format having total length at most 10 kbp.
# 
# > **Return:** The adjacency list corresponding to O_3. You may return edges in any order.

# In[ ]:


from Bio import SeqIO

k = 3
input_file = 'rosalind_grph.txt' #replace filename with yours

with open(input_file) as f:
    fasta_sequences = list(SeqIO.parse(f, 'fasta'))

for fasta1 in fasta_sequences:
    for fasta2 in fasta_sequences:
        name1, sequence1 = fasta1.id, str(fasta1.seq)
        name2, sequence2 = fasta2.id, str(fasta2.seq)
        if sequence1 == sequence2:
            continue
        suffix = sequence1[-k:]
        prefix = sequence2[:k]
        if prefix == suffix:
            print(name1, name2)

