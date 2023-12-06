"""Introduction to Random Strings."""

from math import log10

seq = 'ACGATACAA'
gcs = '0.129 0.287 0.423 0.476 0.641 0.742 0.783'

likelihoods = []
for gc in gcs.split():
    p = float(gc)/2
    l1 = log10(p)
    l2 = log10(0.5-p)
    table = {'A': l2, 'C': l1, 'G': l1, 'T': l2}

    likelihood = 0
    for sym in seq:
        likelihood += table[sym]
    likelihoods.append(likelihood)
print(' '.join([str(likelihood) for likelihood in likelihoods]))
