from src.rna_transcription import transcribe_dna_to_rna

def run_tests_and_sample() -> None:
    # Test 1: Edge case - an empty DNA string should return an empty RNA string 
    assert transcribe_dna_to_rna("") == ""

    #Test 2: Simple verification string 
    assert transcribe_dna_to_rna("ACGT") == "ACGU"

    #Test 3: Rosalind Sample Dataset
    sample_dna = "GATGGAACTTGACTACGTAAATT"
    expected_rna = "GAUGGAACUUGACUACGUAAAUU"

    #Calculate rna using reusable function
    result_rna = transcribe_dna_to_rna(sample_dna)

    # Verify correctness using assert 
    assert result_rna == expected_rna, f"Expected {expected_rna}, got {result_rna}" 

    # Print the transcribed RNA sequence required by Rosalind 
    print(result_rna)

if __name__ == "__main__":
    run_tests_and_sample()