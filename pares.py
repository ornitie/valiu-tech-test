def pares():
    a = [1, 3, 2, 5, 4]
    sorted_a = sorted(a)
    n = 5
    ans = 0

    for i in range(n):
        ans += 1 if a[i] != sorted_a[i] else 0

    return ans//2


if __name__ == "__main__":
    pares()
