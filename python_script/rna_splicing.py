#!/usr/bin/env python
# coding: utf-8

# # RNA Splicing
# 
# ## Genes are Discontiguous
# 
# ### Problem
# 
# After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.
# 
# > **Given:** A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
# 
# > **Return:** A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)

# In[ ]:


with open("rosalind_splc.txt") as fasta:
    nextline = str()
    dict = {}
    for line in fasta:
        if line.startswith(">"):
            header = line.strip(">").strip("\n")
            nextline = ""
            continue
        else:
            nextline += line.strip("\n")
        dict[header] = nextline


# In[ ]:


list = []
for value in dict.values():
    list.append(value)


# In[ ]:


for item in list[1::]:
    list[0] = list[0].replace(item, "")


# In[ ]:


rna_sequence = list[0].replace("T", "U")

map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
    "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

def protein_translation(mRNA):
    start = mRNA.find("AUG")
    triplets = [mRNA[start:start+3] for start in range(start, len(mRNA), 3)]
    for triplet in triplets:
        if map.get(triplet) == "STOP":
            return
        else:
            print(map.get(triplet), end="")
    return


# In[ ]:


protein_translation(rna_sequence)

