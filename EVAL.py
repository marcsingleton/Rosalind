"""Expected Number of Restriction Sites.

Given: A positive integer n (n ≤ 1,000,000), a DNA string s  of even length at most 10, and an array A  of length at
most 20, containing numbers between 0 and 1.

Return: An array B having the same length as A in which B[i] represents the expected number of times that s will appear
as a substring of a random DNA string t of length n, where t is formed with GC-content A[i].
"""

n = 868215
s = 'ATCAGTTCT'
A = '0.000 0.071 0.150 0.195 0.265 0.307 0.360 0.432 0.464 0.537 0.576 0.658 0.703 0.745 0.807 0.853 0.936 1.000'

qs = []
gcs = [float(a) for a in A.split()]
for gc in gcs:
    ps = {'A': (1 - gc) / 2, 'C': gc / 2,
          'G': gc / 2, 'T': (1 - gc) / 2}
    p_match = 1
    for sym in s:
        p_match *= ps[sym]
    q = p_match * (n - len(s) + 1)
    qs.append(q)

print(' '.join([str(q) for q in qs]))