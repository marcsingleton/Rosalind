"""Utility functions for manipulating FASTA files."""


def parse_fasta(file):
    """Read FASTA from file object and return list of headers and sequences.
    
    Refer to read_fasta for details.
    """
    line = file.readline()
    while line:
        if line.startswith('>'):
            header = line.rstrip()
            line = file.readline()

        seqlines = []
        while line and not line.startswith('>'):
            seqlines.append(line.rstrip())
            line = file.readline()
        seq = ''.join(seqlines)
        yield header,seq


def read_fasta(path):
    """Read FASTA file at path and return list of headers and sequences.

    Parameters
    ----------
    path: str
        Path to FASTA file

    Returns
    -------
    fasta: list of tuples of (header, seq)
        The first element is the header line with the >, and the second
        element is the corresponding sequence.
    """
    with open(path) as file:
        yield from parse_fasta(file)
