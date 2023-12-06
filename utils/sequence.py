"""Utility functions for manipulating sequences."""


def reverse_complement(seq):
    """Return the reverse complement of a DNA sequence.

    Parameters
    ----------
    seq: str
        DNA sequence in uppercase.

    Returns
    -------
    rc: str
        Reverse complement.
    """
    pairs = [('A', 'T'), ('G', 'C')]
    table = {**{ord(b1): ord(b2) for b1, b2 in pairs}, **{ord(b2): ord(b1) for b1, b2 in pairs}}
    return seq.upper().translate(table)[::-1]
