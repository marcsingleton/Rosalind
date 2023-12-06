"""Introduction to Alternative Splicing.

Given: Positive integers n and m with 0 ≤ m ≤ n ≤ 2000 .

Return: The sum of combinations C(n, k) for all k satisfying m ≤ k ≤n , modulo 1,000,000.
"""

from math import comb

n = 1637
m = 1121

total = 0
for k in range(m, n+1):
    total += comb(n, k) % int(1E6)
total %= int(1E6)
print(total)
