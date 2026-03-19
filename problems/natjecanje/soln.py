x = input().split()
n = int(x[0])
s = int(x[1])
r = int(x[2])

if (2 <= n <= 10) and (2 <= s <= n) and (1 <= r <= n):
    damaged = list(map(int, input().split()))
    reserve = set(map(int, input().split()))

    answer = 0

    i = 0
    for t in sorted(damaged):
        if t in reserve:
            reserve.remove(t)
        elif t-1 in reserve:
            reserve.remove(t-1)
        elif t+1 in reserve:
            reserve.remove(t+1)
        else:
            answer += 1

    print(answer)
