"""Calculating Protein Mass."""

seq = 'SKADYEK'

aa2weight = {}
with open('constants/aa_weights.txt') as file:
    for line in file:
        aa, weight = line.split()
        aa2weight[aa] = float(weight)

print(sum([aa2weight[sym] for sym in seq]))
