"""Finding a Protein Motif.

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of
locations in the protein string where the motif can be found.
"""

import re
import urllib

data = """\
P0AAM4
P19835_BAL_HUMAN
P06870_KLK1_HUMAN
P01045_KNH2_BOVIN
A4TI59
Q16775
P28314_PER_COPCI
P11831_SRF_HUMAN
P02765_A2HS_HUMAN
Q3Z2Z2
P08514_ITAB_HUMAN
P21735
"""

motif = r'(?=N[^P][ST][^P])'  # Need a lookahead assertion to get overlapping matches

records = []
for name in data.rstrip('\n').split('\n'):
    accession = name.split('_')[0]
    response = urllib.request.urlopen(f'http://www.uniprot.org/uniprot/{accession}.fasta')
    lines = [line.decode('utf-8') for line in response]
    seq = ''.join([line.rstrip('\n') for line in lines[1:]])
    records.append((name, seq))

for name, seq in records:
    matches = list(re.finditer(motif, seq))
    if matches:
        starts = [match.start() + 1 for match in matches]
        print(name)
        print(' '.join([str(start) for start in starts]))
