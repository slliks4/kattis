def main():
    n_test = int(input())

    for _ in range(n_test):
        n, m = map(int, input().split())
        _ = [tuple(map(int, input().split())) for _ in range(m)]
        print(n-1)


if __name__ == "__main__":
    main()
