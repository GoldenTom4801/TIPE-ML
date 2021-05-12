
def fold_left(f, a, liste):
    for b in liste:
        a = f(a, b)
    return a
