def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna);


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna1.find(dna2)


def is_valid_sequence(sequence):
    return count_nucleotides(sequence, 'A') + count_nucleotides(sequence, 'C') +  count_nucleotides(sequence, 'T') + count_nucleotides(sequence, 'G') == get_length(sequence)

def insert_sequence(dna1, dna2, pos):
    return dna1[:pos] + dna2 + dna1[pos:]


def get_complement(dna):
    return {
        'A' : 'T',
        'T' : 'A',
        'C' : 'G',
        'G' : 'C',
    }[dna]

def get_complementary_sequence(dna):
    return dna[::-1]
