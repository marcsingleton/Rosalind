"""Wright-Fisher's Expected Behavior.

Given: A positive integer n (n ≤ 1000000) followed by an array P of length m (m ≤ 20) containing numbers between 0 and
1. Each element of P can be seen as representing a probability corresponding to an allele frequency.

Return: An array B of length m for which B[k] is the expected value of Bin(n, P[k]) ; in terms of Wright-Fisher, it
represents the expected allele frequency of the next generation.
"""

n = 963543
P = '0 0.235846326168 0.245970930566 0.272386897098 0.327089261156 0.333579069144 0.348970284702 0.404237647064 0.456589061833 0.595076758932 0.605288862874 0.719838974521 0.770456255548 0.873245670305 0.925035074137 1'

P = [float(p) for p in P.split()]

E = []
for p in P:
    E.append(n * p)

print(' '.join([str(e) for e in E]))
