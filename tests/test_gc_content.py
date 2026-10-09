from src.gc_content import calculate_gc_content, find_highest_gc

def run_tests_and_sample() -> None:
    # Test 1: Verify GC calculation on a simple 10-base string (4 GC out of 10 = 40.0%)
    assert abs(calculate_gc_content("ATGCATGCAT") - 40.0) < 1e-5

    # Test 2: Rosalind Sample Dataset
    sample_fasta = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"""

    expected_id = "Rosalind_0808"
    expected_gc = 60.919540

    # Execute our function
    best_id, best_gc = find_highest_gc(sample_fasta)

    # Verify ID match and floating point accuracy (within Rosalind tolerance of 0.001)
    assert best_id == expected_id, f"Expected {expected_id}, got {best_id}"
    assert abs(best_gc - expected_gc) < 0.001, f"Expected {expected_gc}, got {best_gc}"

    # Print exact output required by rosalind (ID on line 1, float on line 2)

    print(best_id)
    print(f"{best_gc:.6f}")

if __name__ == "__main__":
    run_tests_and_sample()