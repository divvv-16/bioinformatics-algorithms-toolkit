from src.point_mutation import calculate_hamming_distance

def run_tests_and_sample() -> None:
    # Test1: Edge case - two empty strings have 0 mismatches
    assert calculate_hamming_distance("", "") == 0

    # Test 2: Identical sequences have 0 mismatches
    assert calculate_hamming_distance("GAGC", "GAGC") == 0

    # Test 3: completely mismatched sequence of length 4
    assert calculate_hamming_distance("AAAA", "TTTT") == 4

    # Test 4: Rosalind Sample Dataset
    s = "GAGCCTACTAACGGGAT"
    t = "CATCGTAATGACGGCCT"
    expected_output = 7

    # Calculate output using our function 
    result = calculate_hamming_distance(s, t)

    # Verify correctnesss using assert
    assert result == expected_output, f"Expected{expected_output}, got {result}"

    # Print the calculated Hamming distance required by Rosalind
    print(result)

if __name__ == "__main__":
    run_tests_and_sample()