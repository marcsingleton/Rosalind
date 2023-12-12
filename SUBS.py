"""	Finding a Motif in DNA.

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
"""

s = 'GATATATGCATATACTT'
t = 'ATAT'

indexes = []
for i in range(len(s)):
    if s[i:i+len(t)] == t:
        indexes.append(str(i + 1))
print(' '.join(indexes))
