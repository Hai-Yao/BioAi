# check if a given DNA sequence is valid
def is_valid_dna(seq):
    valid_nucleotides = set("ATCG")
    for nucleotide in seq:
        if nucleotide not in valid_nucleotides:
            return False
    return True

# calculate the GC content of a given sequence
def gc_content(seq):
    gc_count = seq.count("G") + seq.count("C")
    gc_percentage = gc_count / len(seq) * 100
    return round(gc_percentage, 2)

# calculate the reverse complement of a given sequence
def reverse_complement(seq):
    complement = {'A': 'T', 'T':'A', 'C':'G', 'G':'C'}
    rev_comp = ''.join(complement[nucleotide] for nucleotide in reversed(seq))
    return rev_comp

# find motifs in a given sequence
def find_motif(seq, motif):
    positions = []
    motif_length = len(motif)
    for i in range(len(seq) - motif_length +1):
        if seq[i:i+motif_length] == motif:
            positions.append(i)
    return positions

def read_fasta(fasta_file):
    sequences = {}
    with open(fasta_file) as f:
        header = None
        seq_lines = []
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if header:
                    sequences[header] = "".join(seq_lines)
                header = line[1:]
                seq_lines = []
            else:
                seq_lines.append(line)
        if header:
            sequences[header] = "".join(seq_lines)
    return sequences

# calculate the length of each sequence in a fasta file
def sequence_lengths(fasta_file):
    sequences = read_fasta(fasta_file)
    lengths = {header: len(seq) for header, seq in sequences.items()}
    return lengths

# calculate the GC content of each sequence in a fasta file
def sequence_gc_content(fasta_file):
    sequences = read_fasta(fasta_file)
    gc_contents = {header: gc_content(seq) for header, seq in sequences.items()}
    return gc_contents

#find the highest GC content sequence in a fasta file
def highest_gc_content(fasta_file):
    gc_contents = sequence_gc_content(fasta_file)
    for header, gc in gc_contents.items():
        if gc == max(gc_contents.values()):
            return header, gc

## filter sequences based on length
def filter_sequences(fasta_file):
    sequences = read_fasta(fasta_file)
    min_length = 20
    filter_sequences = {}
    for header, seq in sequences.items():
        if len(seq) >= 20:
            filter_sequences[header] = seq
    return filter_sequences

# summary
def summary(fasta_file, output_file):
    sequences = read_fasta(fasta_file)

    #check if the sequence is valid
    for header, seq in sequences.items():
        if False == is_valid_dna(seq):
            print(f"Invalid sequence found: {header}, {seq}")
            return
    print(f"All sequences are valid")

    #calculate the number of sequences
    num_sequences = len(sequences)
    print(f"Number of sequences: {num_sequences}")
    
    #find the highest GC content sequence
    highest_gc_content(fasta_file)
    print(f"Highest GC sequence: {header}, {gc}%")

    #filter sequences based on length
    print(f"sequences longer than 20: {filter_sequences(fasta_file)}")

    with open(output_file, "w") as f_out:
        f_out.write("sequence_id\tlength\tgc_contents\n")
        for header, seq in sequences.items():
            f_out.write(f"{header}\t{len(seq)}\t{gc_content(seq)}\n")
    print(f"summary written to {output_file}")
