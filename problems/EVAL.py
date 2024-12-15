"""Expected Number of Restriction Sites.

Given: A positive integer n (n ≤ 1,000,000), a DNA string s  of even length at most 10, and an array A  of length at
most 20, containing numbers between 0 and 1.

Return: An array B having the same length as A in which B[i] represents the expected number of times that s will appear
as a substring of a random DNA string t of length n, where t is formed with GC-content A[i].

Sample input:
10
AG
0.25 0.5 0.75

Sample output:
0.422 0.563 0.422
"""

n = 10
s = 'AG'
A = '0.25 0.5 0.75'

qs = []
gcs = [float(a) for a in A.split()]
for gc in gcs:
    ps = {
        'A': (1 - gc) / 2,
        'C': gc / 2,
        'G': gc / 2,
        'T': (1 - gc) / 2,
    }
    p_match = 1
    for sym in s:
        p_match *= ps[sym]
    q = p_match * (n - len(s) + 1)
    qs.append(q)

print(' '.join([str(q) for q in qs]))
