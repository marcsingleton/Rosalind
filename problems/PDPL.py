"""Creating a Restriction Map.

Given: A multiset L containing (n2) positive integers for some positive integer n.

Return: A set X containing n nonnegative integers such that ΔX=L.

Sample input:
2 2 3 3 4 5 6 7 8 10

Sample output:
0 2 4 7 10
"""


def partial_digest(L):
    """Return a restriction map for a list of digested fragments.

    Algorithm is adapted from An Introduction to Bioinformatics Algorithms by Jones and Pevzner.

    The core logic is that at each step the largest difference must be between one of the two endpoints. The algorithm
    checks for both possibilities in a recursive fashion until exhausting all differences, or it makes an incorrect
    choice.
    """
    L = L.copy()
    width = max(L)
    X = [0, width]
    L.remove(width)
    Xs = []
    place(L, X, Xs, width)
    return Xs


def place(L, X, Xs, width):
    if not L:
        Xs.append(X)
        return
    ys = [max(L), width - max(L)]
    for y in ys:
        D = delta(y, X)
        if is_subset(D, L):
            L_copy, X_copy = L.copy(), X.copy()
            X_copy.append(y)
            for d in D:
                L_copy.remove(d)
            place(L_copy, X_copy, Xs, width)
    return


def delta(y, X):
    D = []
    for x in X:
        if y > x:
            d = y - x
        else:
            d = x - y
        D.append(d)
    return D


def is_subset(X, Y):
    X_counts = {}
    for x in X:
        X_counts[x] = X_counts.get(x, 0) + 1
    Y_counts = {}
    for y in Y:
        Y_counts[y] = Y_counts.get(y, 0) + 1
    for value, x_count in X_counts.items():
        y_count = Y_counts.get(value, 0)
        if x_count > y_count:
            return False
    return True


data = '2 2 3 3 4 5 6 7 8 10'

L = [int(value) for value in data.split()]

Xs = partial_digest(L)
for X in Xs:
    print(' '.join([str(x) for x in X]))
