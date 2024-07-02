"""Mortal Fibonacci Rabbits.

Given: Positive integers n ≤ 100 and m ≤ 20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
"""

from functools import cache


@cache
def fibo(n, m):
    if n <= 0:
        return 0, 0
    if n == 1:
        return 1, 0  # 1 juvenile at gen1
    if n == 2:
        return 0, 1  # 1 adult at gen2
    else:
        j1, a1 = fibo(n - 1, m)  # adult and juvenile counts in previous gen
        jm, _ = fibo(n - m, m)  # number of juveniles m generations before
        a0 = a1 + j1 - jm  # subtract adults of age m from total adults
        return a1, a0


n, m = 6, 3
print(sum(fibo(n, m)))
