
dna_seq = '''ATGTACTCATTCGTTTCGGAAGAGACAGGTACGTTAATAGTTAATAGCGTACTTCTTTTTCTTGCTTTCG
TGGTATTCTTGCTAGTTACACTAGCCATCCTTACTGCGCTTCGATTGTGTGCGTACTGCTGCAATATTGT
TAACGTGAGTCTTGTAAAACCTTCTTTTTACGTTTACTCTCGTGTTAAAAATCTGAATTCTTCTAGAGTT
CCTGATCTTCTGGTCTAA'''

a=dna_seq.count('G')
b=dna_seq.count('C')
c=len(dna_seq)
gc_percent = ((a+b)/c*100)


print(gc_percent.__round__(2))
print(round(gc_percent,2))

print(gc_percent.__round__(1))
print(round(gc_percent,1))

print(f'The GC content in this DNA sequence is {round(gc_percent,1)} %.')