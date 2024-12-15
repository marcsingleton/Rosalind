"""Ordering Strings of Varying Length Lexicographically.

Given: A permutation of at most 12 symbols defining an ordered alphabet 𝒜 and a positive integer n ( n≤ 4).

Return: All strings of length at most n formed from 𝒜, ordered lexicographically. (Note: As in “Enumerating k-mers
Lexicographically”, alphabet order is based on the order in which the symbols are given.)

Sample input:
D N A
3

Sample output:
D
DD
DDD
DDN
DDA
DN
DND
DNN
DNA
DA
DAD
DAN
DAA
N
ND
NDD
NDN
NDA
NN
NND
NNN
NNA
NA
NAD
NAN
NAA
A
AD
ADD
ADN
ADA
AN
AND
ANN
ANA
AA
AAD
AAN
AAA
"""

from itertools import product

alphabet = 'D N A'
n = 3

alphabet = alphabet.split()
order = {sym: i for i, sym in enumerate(alphabet)}

perms = []
for k in range(1, n + 1):
    for perm in product(*[alphabet for i in range(k)]):
        perms.append(perm)

for perm in sorted(perms, key=lambda xs: [order[x] for x in xs]):
    print(''.join(perm))
