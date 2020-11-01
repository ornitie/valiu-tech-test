def celadores():
    A = [1, 2, 8]
    B = [9, 5, 9]
    m = 10
    n = 3

    A, B = zip(*sorted(zip(A, B)))
    A = list(A)
    B = list(B)

    ans = (A[0] - 1) + (m - max(B))

    for i in range(1, n):
        if B[i-1] >= B[i]:
            A[i] = A[i-1]
            B[i] = B[i-1]
        ans += A[i] - B[i-1] - 1 if A[i] > B[i-1] else 0

    return ans


if __name__ == "__main__":
    celadores()
