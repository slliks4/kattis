import sys

MOD = 10**9 + 7
MAXN = 10000

x = [0] * (MAXN + 1)
x[1] = 2
x[2] = 3

for i in range(3, MAXN + 1):
    x[i] = (x[i - 1] + x[i - 2]) % MOD

data = sys.stdin.read().strip().split()
T = int(data[0])
idx = 1

out = []
for _ in range(T):
    n = int(data[idx])
    idx += 1
    out.append(str(x[n]))

print("\n".join(out))
