# https://open.kattis.com/problems/subsequencesinsubstrings

def compute(s, t):
    n = len(s)
    m = len(t)
    count = 0

    for L in range(n):
        j = 0  # pointer for t
        for R in range(L, n):
            if s[R] == t[j]:
                j += 1
                if j == m:
                    count += (n - R)
                    break

    return count


def main():
    s = input()
    t = input()

    print(compute(s, t))


if __name__ == "__main__":
    main()
