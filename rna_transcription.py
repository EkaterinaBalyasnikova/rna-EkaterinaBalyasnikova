def to_rna(dna_strand):
    dna_strand = dna_strand.replace('A','U')
    dna_strand = dna_strand.replace('C','F')
    dna_strand = dna_strand.replace('G','C')
    dna_strand = dna_strand.replace('F','G')
    dna_strand = dna_strand.replace('T','A')
    return dna_strand
