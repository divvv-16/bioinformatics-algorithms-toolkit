from typing import Dict, Tuple
def parse_fasta(fasta_text: str) -> Dict[str, str]:
    """
    Parses a multi-line FASTA format string into a dictionary mapping sequence IDs to their full DNA sequences.
    """
    sequences: Dict[str, str] = {}
    current_id = ""

    for line in fasta_text.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            current_id = line[1:].strip() # Strip off the leading '>'
            sequences[current_id] = ""
        elif current_id:
            sequences[current_id] += line.strip().upper()

    return sequences

def calculate_gc_content(dna: str) -> float:
    """
    Calculates the GC content percentage of a DNA sequence.
    """
    if not dna:
        return 0.0

    gc_count = dna.count("G") + dna.count("C")
    return (gc_count / len(dna)) * 100

def find_highest_gc(fasta_text: str) -> Tuple[str, float]:
    """
    Finds the FASTA record with the highest GC-content.
    
    Returns:
        Tuple[str, float]: (highest_id, highest_gc_percentage)
    """
    parsed_seqs = parse_fasta(fasta_text)

    highest_id = ""
    highest_gc = -1.0

    for seq_id, dna in parsed_seqs.items():
        gc_val = calculate_gc_content(dna)
        if gc_val > highest_gc:
            highest_gc = gc_val
            highest_id = seq_id
    return (highest_id, highest_gc)