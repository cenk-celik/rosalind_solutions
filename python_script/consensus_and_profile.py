#!/usr/bin/env python
# coding: utf-8

# # Consensus and Profile
# ## Problem
# 
# A matrix is a rectangular table of values divided into rows and columns. An **m × n** matrix has **m** rows and **n** columns. Given a matrix **A**, we write A_i,j to indicate the value found at the intersection of row **i** and column **j**.
# 
# Say that we have a collection of DNA strings, all having the same length **n**. Their profile matrix is a **4 × n** matrix **P** in which **P_1,j** represents the number of times that 'A' occurs in the **j-th** position of one of the strings, **P_2,j** represents the number of times that 'C' occurs in the **j-th** position, and so on.
# 
# A consensus string **c** is a string of length **n** formed from our collection by taking the most common symbol at each position; the **j-th** symbol of **c** therefore corresponds to the symbol having the maximum value in the **j-th** column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.
# 
# ----------------------
# |    DNA strings    |
# ---------------------
# |	A T C C A G C T |
# |	G G G C A A C T |
# |	A T G G A T C T |
# |   A A G C A A C C |
# |	T T G G A A C T |
# |	A T G C C A T T |
# |	A T G G C A C T |
#  
# ----
# | Profile |
# ----------------
# | **A**   5 1 0 0 5 5 0 0 |
# | **C**   0 0 1 4 2 0 6 1 |
# | **G**   1 1 6 3 0 1 0 0 |
# | **T**   1 5 0 0 0 1 1 6 |
# 
# **Consensus**	A T G C A A C T
# 
# > **Given:** A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# 
# > **Return:** A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

# In[ ]:


def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))


# In[ ]:


data_list = []
file = open('main.out','w')
with open('rosalind_cons.txt') as fp: #replace filename with yours
    for name, seq in read_fasta(fp):
        data_list.append(seq)
length = len(data_list)
# length of string
L = len(seq)

P = [[0 for x in xrange(L)] for y in xrange(4)] 

Q = ['A','C','G','T']

for x in range(L):
    for y in range(4):
        for z in range(length):
            P[y][x] = P[y][x] + data_list[z][x].count(Q[y])

domi = ""
for x in range(L):
    MAX = 0
    for y in range(4):  
        if P[y][x]>=P[MAX][x]:
            MAX = y       
            
    if MAX == 0:
        domi = domi+'A'
    elif MAX ==1:
        domi = domi+'C'
    elif MAX ==2:
        domi = domi+'G'
    elif MAX ==3:
        domi = domi+'T'


# In[ ]:


file.write('%s\n%s\n%s\n%s\n%s' %(
    domi,'A: '+str(P[0]).strip('[]').replace(',',''),'C: '
    +str(P[1]).strip('[]').replace(',',''),'G: '
    +str(P[2]).strip('[]').replace(',',''),'T: '
    +str(P[3]).strip('[]').replace(',','')))

