"""Finding a Protein Motif.

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of
locations in the protein string where the motif can be found.

Sample input:
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST

Sample output:
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
"""

import re
import urllib

data = """\
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST
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
