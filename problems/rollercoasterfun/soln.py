import sys


def solve():
    in_d = sys.stdin.read().split()
    if not in_d:
        return

    idx = 0
    N = int(in_d[idx])
    idx += 1

    max_l = 25000
    dp = [0] * (max_l + 1)

    for _ in range(N):
        a = int(in_d[idx])
        b = int(in_d[idx+1])
        t = int(in_d[idx+2])
        idx += 3

        if b == 0:
            for j in range(t, max_l + 1):
                if dp[j - t] + a > dp[j]:
                    dp[j] = dp[j - t] + a
        else:
            k = 1
            while True:
                fun_value = a - (k - 1)**2 * b
                if fun_value <= 0:
                    break

                for j in range(max_l, t - 1, -1):
                    if dp[j - t] + fun_value > dp[j]:
                        dp[j] = dp[j - t] + fun_value
                k += 1

    for i in range(1, max_l + 1):
        if dp[i-1] > dp[i]:
            dp[i] = dp[i-1]

    Q = int(in_d[idx])
    idx += 1
    results = []
    for _ in range(Q):
        T_i = int(in_d[idx])
        idx += 1
        results.append(str(dp[T_i]))

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    solve()
