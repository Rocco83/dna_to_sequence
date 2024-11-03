#!/usr/bin/python3

def translate_codon(codon):
    codon_table = {
        'AAA': 'Lys', 'AAC': 'Asn', 'AAG': 'Lys', 'AAT': 'Asn',
        'ACA': 'Thr', 'ACC': 'Thr', 'ACG': 'Thr', 'ACT': 'Thr',
        'AGA': 'Arg', 'AGC': 'Ser', 'AGG': 'Arg', 'AGT': 'Ser',
        'ATA': 'Ile', 'ATC': 'Ile', 'ATG': 'Met', 'ATT': 'Ile',
        'CAA': 'Gln', 'CAC': 'His', 'CAG': 'Gln', 'CAT': 'His',
        'CCA': 'Pro', 'CCC': 'Pro', 'CCG': 'Pro', 'CCT': 'Pro',
        'CGA': 'Arg', 'CGC': 'Arg', 'CGG': 'Arg', 'CGT': 'Arg',
        'CTA': 'Leu', 'CTC': 'Leu', 'CTG': 'Leu', 'CTT': 'Leu',
        'GAA': 'Glu', 'GAC': 'Asp', 'GAG': 'Glu', 'GAT': 'Asp',
        'GCA': 'Ala', 'GCC': 'Ala', 'GCG': 'Ala', 'GCT': 'Ala',
        'GGA': 'Gly', 'GGC': 'Gly', 'GGG': 'Gly', 'GGT': 'Gly',
        'GTA': 'Val', 'GTC': 'Val', 'GTG': 'Val', 'GTT': 'Val',
        'TAA': 'Stop', 'TAC': 'Tyr', 'TAG': 'Stop', 'TAT': 'Tyr',
        'TCA': 'Ser', 'TCC': 'Ser', 'TCG': 'Ser', 'TCT': 'Ser',
        'TGA': 'Stop', 'TGC': 'Cys', 'TGG': 'Trp', 'TGT': 'Cys',
        'TTA': 'Leu', 'TTC': 'Phe', 'TTG': 'Leu', 'TTT': 'Phe'
    }
    return codon_table.get(codon, 'Unknown')

def annotate_dna_sequence(filename):
    with open(filename, 'r') as file:
        dna_sequence = file.read().strip()

    codon_length = 3
    protein_sequence = []
    nucleotide_position = 1

    for i in range(0, len(dna_sequence), codon_length):
        codon = dna_sequence[i:i+codon_length]
        amino_acid = translate_codon(codon)
        protein_sequence.append(amino_acid)

        start_pos = nucleotide_position
        end_pos = nucleotide_position + codon_length - 1
        nucleotide_positions = f"{start_pos}-{end_pos}"

        line = f"{amino_acid}\t{len(protein_sequence)}\t{codon}\t{start_pos}-{end_pos}"
        print(line)
        nucleotide_position += codon_length

filename = "champ1_raw"  # Replace with your DNA sequence file
annotate_dna_sequence(filename)
