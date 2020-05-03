#!/usr/bin/env python
# coding: utf-8

# # Open Reading Frames
# ## Problem
# 
# Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.
# 
# An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.
# 
# > **Given:** A DNA string **s** of length at most 1 kbp in FASTA format.
# 
# > **Return:** Every distinct candidate protein string that can be translated from ORFs of **s.** Strings can be returned in any order.

# In[ ]:


dna_codon_table = {
    "TTT":"F", "CTT":"L", "ATT":"I", "GTT":"V",
    "TTC":"F", "CTC":"L", "ATC":"I", "GTC":"V",
    "TTA":"L", "CTA":"L", "ATA":"I", "GTA":"V",
    "TTG":"L", "CTG":"L", "ATG":"M", "GTG":"V",
    "TCT":"S", "CCT":"P", "ACT":"T", "GCT":"A",
    "TCC":"S", "CCC":"P", "ACC":"T", "GCC":"A",
    "TCA":"S", "CCA":"P", "ACA":"T", "GCA":"A",
    "TCG":"S", "CCG":"P", "ACG":"T", "GCG":"A",
    "TAT":"Y", "CAT":"H", "AAT":"N", "GAT":"D",
    "TAC":"Y", "CAC":"H", "AAC":"N", "GAC":"D",
    "TAA":"STOP", "CAA":"Q", "AAA":"K", "GAA":"E",
    "TAG":"STOP", "CAG":"Q", "AAG":"K", "GAG":"E",
    "TGT":"C", "CGT":"R", "AGT":"S", "GGT":"G",
    "TGC":"C", "CGC":"R", "AGC":"S", "GGC":"G",
    "TGA":"STOP", "CGA":"R", "AGA":"R", "GGA":"G",
    "TGG":"W", "CGG":"R", "AGG":"R", "GGG":"G"
}


# In[ ]:


def complementary_dna(dna_string):
    replace_bases = {"A":"T","T":"A","G":"C","C":"G"}
    return ''.join([replace_bases[base] for base in reversed(dna_string)])


# In[ ]:


def translate(fragment):
    peptide = []
    methionine = fragment.find("ATG")
    codons = [fragment[methionine:methionine+3] for methionine in range(methionine, len(fragment), 3)]
    for codon in codons:
        peptide += dna_codon_table.get(codon)
    return ''.join(map(str, peptide)) 


# In[ ]:


with open("rosalind_orf.txt") as file:
    for line in file:
        if line.startswith(">"):
            nextline = str()
        else:
            nextline += (line.strip("\n"))
    dna_string = nextline


# In[ ]:


import re

pattern = re.compile(r'(?=(ATG(?:...)*?)(?=TAA|TAG|TGA))')

fragments = []
for string in re.findall(pattern, dna_string):
    fragments.append(string)

for string in re.findall(pattern, complementary_dna(dna_string)):
    fragments.append(string)


# In[ ]:


for string in set(fragments):
    print(translate(string))

