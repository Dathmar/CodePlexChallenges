dna2rna_dict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

def dna2rna(dna):
    rna = ''
    for nucleotide in dna:
        rna += dna2rna_dict[nucleotide]

    return rna

print(dna2rna('GCTATGGCTA'))