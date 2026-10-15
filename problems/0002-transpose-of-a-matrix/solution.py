
def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    if not a:
        return []

    return [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]
