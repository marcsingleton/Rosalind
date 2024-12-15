"""Transcribing DNA into RNA.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

Sample input:
GATGGAACTTGACTACGTAAATT

Sample output:
GAUGGAACUUGACUACGUAAAUU
"""

seq = 'GATGGAACTTGACTACGTAAATT'

print(seq.replace('T', 'U'))
