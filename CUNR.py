"""Counting Unrooted Binary Trees

Given: A positive integer n (n ≤ 1000).

Return: Let b(n) denote the total number of distinct unrooted binary trees having n labeled leaves. The value of b(n)
modulo 1,000,000.
"""

n = 857
mod = int(1E6)

e = 2 * (n - 1) - 3
b = 1
for i in range(e, 1, -2):
    b *= i
    b %= mod

print(b)
