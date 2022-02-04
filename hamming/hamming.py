"""
    Hamming exercise
"""

def distance(strand_a, strand_b):
    """
        Return the hamming distance between two DNA
    """

    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return [strand_a[index] != strand_b[index] for index in range(len(strand_b))].count(True)
