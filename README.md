# bioinformatics-algorithms-toolkit
Modular Python implementation of bioinformatics sequence analysis algorithms with full unit testing.
def calculate_gc_content(sequence: str) -> float:
    """Calculates the GC-content percentage of a given DNA sequence."""
    clean_seq = sequence.upper()
    g_count = clean_seq.count("G")
    c_count = clean_seq.count("C")
    total_length = len(clean_seq)

    if total_length == 0:
        return 0.0

    return ((g_count + c_count) / total_length) * 100