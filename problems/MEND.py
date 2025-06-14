"""Inferring Genotype from a Pedigree.

Given: A rooted binary tree T in Newick format encoding an individual's pedigree for a Mendelian factor whose alleles
are A (dominant) and a (recessive).

Return: Three numbers between 0 and 1, corresponding to the respective probabilities that the individual at the root of
T will exhibit the "AA", "Aa" and "aa" genotypes.


Sample input:
((((Aa,aa),(Aa,Aa)),((aa,aa),(aa,AA))),Aa);

Sample output:
0.156 0.5 0.344
"""

from utils import TreeNode

data = """\
((((Aa,aa),(Aa,Aa)),((aa,aa),(aa,AA))),Aa);
"""

genotypes = ('AA', 'Aa', 'aa')

tree = TreeNode.from_newick(data)

for node in tree.traverse(order='post'):
    if node.is_tip():
        ps = {geno: 0 for geno in genotypes}
        ps[node.name] = 1
        node.ps = ps
    else:
        child1, child2 = node.children
        pA1 = child1.ps['AA'] + 0.5 * child1.ps['Aa']
        pA2 = child2.ps['AA'] + 0.5 * child2.ps['Aa']
        pa1 = 1 - pA1
        pa2 = 1 - pA2
        ps = {
            'AA': pA1 * pA2,
            'Aa': pA1 * pa2 + pa1 * pA2,
            'aa': pa1 * pa2,
        }
        node.ps = ps

print(' '.join([str(value) for value in tree.ps.values()]))
