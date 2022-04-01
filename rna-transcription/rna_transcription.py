"""
    RNA Transcription exercise
"""
RNA = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U"
}

def to_rna(dna_strand):
    """
        Get transcription
    """
    return "".join(map(lambda x: RNA[x], list(dna_strand)))
