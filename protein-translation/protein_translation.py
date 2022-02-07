"""
    Protein Translation Exercise
"""

from textwrap import wrap

def proteins(strand):
    """
        Return a list of Amino Acids from strand
    """

    dct = {}
    for codons in ["UCU", "UCC", "UCA", "UCG"]:
        dct[codons] = "Serine"
    for codons in ["UUU", "UUC"]:
        dct[codons] = "Phenylalanine"
    for codons in ["UUA", "UUG"]:
        dct[codons] = "Leucine"
    for codons in ["UAU", "UAC"]:
        dct[codons] = "Tyrosine"
    for codons in ["UGU", "UGC"]:
        dct[codons] = "Cysteine"
    for codons in ["UAA", "UAG", "UGA"]:
        dct[codons] = "STOP"
    dct["AUG"], dct["UGG"] = "Methionine", "Tryptophan"
    result = []
    for item in wrap(strand, 3):
        if dct[item] == "STOP":
            break
        result.append(dct[item])
    return result
