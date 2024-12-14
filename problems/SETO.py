"""Introduction to Set Operations.

Given: A positive integer n (n ≤ 20,000) and two subsets A and B of {1, 2, …, n}.

Return: Six sets: A∪B, A∩B, A−B, B−A, Ac, and Bc (where set complements are taken with respect to {1, 2, …, n}).
"""

n = 10
A = {1, 2, 3, 4, 5}
B = {2, 8, 5, 10}

U = {i + 1 for i in range(n)}
print(A.union(B))
print(A.intersection(B))
print(A - B)
print(B - A)
print(U - A)
print(U - B)
