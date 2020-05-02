#!/usr/bin/env python
# coding: utf-8

# # Translating RNA into Protein
# ## Problem
# 
# The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.
# 
# The [RNA codon table](https://en.wikipedia.org/wiki/Genetic_code#RNA_codon_table) dictates the details regarding the encoding of specific codons into the amino acid alphabet.
# 
# > **Given:** An RNA string **s** corresponding to a strand of mRNA (of length at most 10 kbp).
# 
# > **Return:** The protein string encoded by **s**.

# In[ ]:


#first, create a dictionary of RNA codon table
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


# In[ ]:


#define a function to translate codons into proteins
def translate_mrna(mRNA):
    start = mRNA.find("AUG")
    triplets = [mRNA[start:start+3] for start in range(start, len(mRNA), 3)]
    for triplet in triplets:
        if map.get(triplet) == "STOP":
            return
        else:
            print(map.get(triplet), end="")
    return


# In[ ]:


with open("rosalind_prot.txt","r") as mrna_data:
    mRNA = str(mrna_data.readlines())
    translate_mrna(mRNA)

