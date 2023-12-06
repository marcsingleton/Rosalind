"""Matching Random Motifs."""

N = 97023
gc = 0.515636
s = 'TCCAACATA'

ps = {'A': (1-gc)/2, 'C': gc/2,
      'G': gc/2, 'T': (1-gc)/2}

p_match = 1
for sym in s:
    p_match *= ps[sym]

q = 1 - (1 - p_match) ** N
print(q)
