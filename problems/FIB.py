"""Rabbits and Recurrence Relations.

Given: Positive integers n ≤ 40 and k ≤ 5.

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each
generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

Sample input:
5 3

Sample output:
19
"""

from functools import cache


@cache
def fibo(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n - 1, k) + k * fibo(n - 2, k)


n, k = 5, 3
print(fibo(n, k))
