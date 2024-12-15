"""Calculating Expected Offspring.

Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples
in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the
number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa

Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption
that every couple has exactly two offspring.

Sample input:
1 0 0 1 0 1

Sample output:
3.5
"""

from itertools import product

data = '1 0 0 1 0 1'

couples = [
    ('AA', 'AA'),
    ('AA', 'Aa'),
    ('AA', 'aa'),
    ('Aa', 'Aa'),
    ('Aa', 'aa'),
    ('aa', 'aa'),
]
dominant = 0
for count, couple in zip(data.split(), couples):
    parent1, parent2 = couple
    offsprings = []
    for allele1, allele2 in product(parent1, parent2):
        if allele1 == 'A' or allele2 == 'A':
            dominant += (
                0.5 * int(count)
            )  # Each offspring has probability 0.25, so with 2 offspring the expected count is 0.5 per couple
print(dominant)
