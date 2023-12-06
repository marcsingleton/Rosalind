"""Counting Subsets."""

n = 850

total = 1
for _ in range(n):
    total = 2 * total % 1E6
print(total)