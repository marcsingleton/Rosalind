"""Inferring Protein from Spectrum.

Given: A list L of n (n ≤ 100) positive real numbers.

Return: A protein string of length n−1 whose prefix spectrum is equal to L (if multiple solutions exist, you may output
any one of them). Consult the monoisotopic mass table.
"""

data = """\
3524.8542
3710.9335
3841.974
3970.0326
4057.0646
"""

aa2weight = {}
with open('constants/aa_weights.txt') as file:
    for line in file:
        aa, weight = line.split()
        aa2weight[aa] = float(weight)

spectrum = [float(value) for value in data.split()]
weights = [spectrum[i+1] - spectrum[i] for i in range(len(spectrum)-1)]

seq = []
for weight in weights:
    aa = min(aa2weight, key=lambda x: abs(weight-aa2weight[x]))
    seq.append(aa)

print(''.join(seq))
