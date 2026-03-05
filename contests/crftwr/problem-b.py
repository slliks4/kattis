import math
m = int(input())
c = list(map(int, input().split()))
n, e = map(int, input().split())

tp = {}
belt = [math.inf] * (n+1)
teams = [0] * n

for i in range(e):
    t,p = map(int, input().split())
    tp.setdefault(t, []).append(p)

start = 0
menu_idx = 0

for j in range(max(tp) + 1):
    start = (start - 1) % len(belt)

    if belt[start] == math.inf:
        belt[start] = c[menu_idx]
        menu_idx = (menu_idx + 1) % len(c)

    if j in tp:
        for k in tp[j]:
            idx = (start + k) % len(belt)
            teams[k - 1] += belt[idx]
            belt[idx] = math.inf

for team in teams:
    print(team)
