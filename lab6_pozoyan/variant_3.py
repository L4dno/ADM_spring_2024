def stella_algorithm(permutation):
    n = len(permutation)
    z = [0] * ( n + 2)
    p = [0] * (n + 2)
    d = [0] * (n + 2)

    for i in range(1, n + 1):
        z[i] = permutation[i - 1]
        p[i] = i
        d[i] = -1

    d[1] = 0
    m = n + 1
    z[0] = m
    z[n + 1] = m

    k = 0

    while m != 1:
        k += 1
        print(f"{' '.join(map(str, z[1:n + 1]))}")

        m = n
        while z[p[m] + d[m]] > m:
            d[m] = -d[m]
            m -= 1

        pm = p[m]
        dm = pm + d[m]
        w = z[pm]
        z[pm] = z[dm]
        z[dm] = w

        zpm = z[pm]
        w = p[zpm]
        p[zpm] = pm
        p[m] = w

    return k

def main():
    n = int(input("Введите n: "))
    print(f"\nПерестановки при n = {n}")
    initial_permutation = list(range(1, n + 1))
    total_permutations = stella_algorithm(initial_permutation)
    print(f"\nОбщее количество перестановок: {total_permutations}")

if __name__ == "__main__":
    main()
