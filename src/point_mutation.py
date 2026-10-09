def calculate_hamming_distance(s: str, t: str) -> int:
    """ 
    Calculates the Hamming distance (number of point mutation mismatches) between two DNA sequence strings of equal length.
    
    Parameters:
        s (str): First DNA sequence string.
        t (str): Second DNA sequence string.
        
    Returns:
        int: Total number of mismatched positions between s and t.
        
    Raises: 
        ValueError: If sequence lengths do not match.
    """
    # Step 2: Clean whitespace and convert to uppercase
    clean_s = s.strip().upper()
    clean_t = t.strip().upper()

    # Step 2: Ensure both sequeences are of equal length
    if len(clean_s) != len(clean_t):
        raise ValueError("Sequence must be of equal length to calculate Hamming distance.")

    # Step 3: Zip sequences together and sum all mismatched positions
    mismatches = sum(1 for base_s, base_t in zip(clean_s, clean_t) if base_s != base_t)

    return mismatches