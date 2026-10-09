from src.dna_reverse_complement import reverse_complement

def run_tests_and_sample() -> None:
    # Test 1: Edge case - empty string should return an empty string 
    assert reverse_complement("") == ""

    # Test 2: Short verification sequence ("GTCA" reverse complement is "TGAC")
    assert reverse_complement("GTCA") == "TGAC"

    # Test 3: Rosalind Sample Dataset
    sample_dna = "AAAACCCGGT"
    expected_output = "ACCGGGTTTT"

    # Calculate output using our reusable function 
    result = reverse_complement(sample_dna)

    # Verify correctness using assert
    assert result == expected_output, f"Expected {expected_output}, got {result}"

    # Print the reverse complement required by Rosalind 
    print(result)

if __name__ == "__main__":
    run_tests_and_sample()