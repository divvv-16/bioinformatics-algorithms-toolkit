from typing import Tuple


def count_nucleotides(dna: str) -> Tuple[int, int, int, int]:
    """
    Count the number of nucleotides in a DNA string.

    Parameters:
    dna (str): A string representing the DNA nucleotides (e.g., 'AGCT')

    Returns:
    Tuple[int, int, int, int]: A tuple containing the counts of 'A', 'C', 'G', and 'T' in order.   
    """
    # Remove any surrounding whitespace or newlines
    clean_dna = dna.strip()

    #Use str.count() to tally each nucleotide base
    a_count = clean_dna.count('A')
    c_count = clean_dna.count('C')
    g_count = clean_dna.count('G')
    t_count = clean_dna.count('T')

    return a_count, c_count, g_count, t_count
