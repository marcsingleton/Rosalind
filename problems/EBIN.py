"""Wright-Fisher's Expected Behavior.

Given: A positive integer n (n ≤ 1000000) followed by an array P of length m (m ≤ 20) containing numbers between 0 and
1. Each element of P can be seen as representing a probability corresponding to an allele frequency.

Return: An array B of length m for which B[k] is the expected value of Bin(n, P[k]) ; in terms of Wright-Fisher, it
represents the expected allele frequency of the next generation.

Sample input:
17
0.1 0.2 0.3

Sample output:
1.7 3.4 5.1
"""

n = 17
P = '0.1 0.2 0.3'

P = [float(p) for p in P.split()]

E = []
for p in P:
    E.append(n * p)

print(' '.join([str(e) for e in E]))
