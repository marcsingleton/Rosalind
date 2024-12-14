"""Mendel's First Law.

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are
homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant
allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
"""

k, m, n = 23, 18, 17

N = k + m + n
p_het = m / N * (m - 1) / (N - 1) / 4  # Two hets mating
p_hom1 = m / N * n / (N - 1)  # Homozygote dominant with het
p_hom2 = n / N * (n - 1) / (N - 1)  # Two homo recessive
p = 1 - p_het - p_hom1 - p_hom2

print(p)
