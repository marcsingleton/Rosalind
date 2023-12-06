"""	Finding a Motif in DNA."""

s = 'GATATATGCATATACTT'
t = 'ATAT'

indexes = []
for i in range(len(s)):
    if s[i:i+len(t)] == t:
        indexes.append(str(i + 1))
print(' '.join(indexes))
