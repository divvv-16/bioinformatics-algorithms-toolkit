def transcribe_dna_to_rna(dna: str) -> str:
    """
    Transcribes a DNA string into an RNA string by replacing all occurrences of 'T' with 'U'.

    Parameters:
    dna (str): A string representing the DNA sequence (e.g., 'GATTACA').

    Returns:
    str: The transcribed RNA sequence string (e.g., 'GAAUACA').
    """
    #Step 1: Clean surrounding whitespace and convert to uppercase
    clean_dna = dna.strip().upper()

    # Step 2: Replace 'T' with 'U' to transcribe DNA to RNA
    rna = clean_dna.replace("T", "U")

    return rna
    