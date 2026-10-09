def reverse_complement(dna: str) -> str:
    """
    Computes the reverse complement of a DNA sequence string.

    Parameters: 
    dna (str): A string representing a DNA sequence (e.g., "AAAACCCGGT").

    Returns:
    str: The reverse complement sequence (e.g., "ACCGGGTTTT").
    """
    # Step 1: Clean surrounding whitespace
    clean_dna = dna.strip()

    # Step 2: Build a simultaneous complement mapping table
    trans_table = str.maketrans("ACGTacgt", "TGCAtgca")

    # Step 3: Complement each base and reverse the resulting string
    complemented = clean_dna.translate(trans_table)
    rev_comp = complemented[::-1]

    return rev_comp