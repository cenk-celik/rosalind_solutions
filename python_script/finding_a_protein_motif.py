#!/usr/bin/env python
# coding: utf-8

# # Finding a Protein Motif
# ## Problem
# 
# To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: \[XY\] means "either **X** or **Y**" and **{X}** means "any amino acid except **X**." For example, the N-glycosylation motif is written as **N{P}\[ST\]{P}**.
# 
# You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into [here](http://www.uniprot.org/uniprot/uniprot_id)
# 
# Alternatively, you can obtain a protein sequence in FASTA format [here](http://www.uniprot.org/uniprot/uniprot_id.fasta)
# 
# For example, the data for protein **B5ZC00** can be found at  [here](http://www.uniprot.org/uniprot/B5ZC00).
# 
# > **Given:** At most 15 UniProt Protein Database access IDs.
# 
# > **Return:** For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

# In[ ]:


import sys
get_ipython().system('{sys.executable} -m pip install requests')
import requests


# In[ ]:


#to access uniprot
url = 'https://www.uniprot.org/uniprot/'

#data to use
with open("rosalind_mprt.txt") as file: #replace filename with yours
    seqIDs = file.read().replace("\n", " ").split()
sequences = {}
for proID in seqIDs:
    goToURL = url+proID+".fasta"
    response = requests.get(goToURL)
    sequences[proID] = (response.text.split("\n")) #get the FASTA sequence into a dict
    sequences[proID] = "".join(sequences[proID][1::]) #skip the first line in FASTA and assing it to protein ID.


# In[ ]:


def N_gly_motif(ID, sequence):
    sequence = list(sequence)
    global result
    result = []
    for i in range(0, len(sequence)-3):
        seq = sequence[i:i+4]
        if (seq[0] == "N") and (seq[2] == "S" or seq[2] == "T") and (seq[1] and seq[3] != "P"):
            result.append(i+1)


# In[ ]:


for key, value in sequences.items():
    N_gly_motif(key, value)
    if not result:
        continue
    else:
        print(key)
        print(*result)

