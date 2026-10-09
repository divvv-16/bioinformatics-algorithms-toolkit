# Import our reusable function from the src module 
from src.dna_operations import count_nucleotides 

def run_tests_and_sample() -> None:
    # 1. Edge-case test: Empty DNA sequence should return all zeroes
    assert count_nucleotides("ACGT") == (1, 1, 1, 1)

    # 2. Short verification test
    assert count_nucleotides("ACGT") == (1, 1, 1, 1)

    # 3. Rosalind Sample Dataset
    sample_dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    expected_output = (20, 12, 17, 21)  # Expected counts of A, C, G, T

    # Verify correctness using assert 
    result_tuple = count_nucleotides(sample_dna)
    assert result_tuple == expected_output, f"Expected {expected_output}, got {result_tuple}"

    # Unpacking (*result_tuple) prints the 4 numbers separated by single spaces print(*result_tuple)

if __name__ == "__main__":
    run_tests_and_sample()
    
