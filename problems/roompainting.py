n, m = map(int, input().split())

can_sizes = []
joe_needs = []

for i in range(n):
    s = input()
    can_sizes.append(int(s))

for j in range(m):
    s = input()
    joe_needs.append(int(s))

can_sizes.sort()

dummy = {}

i = 0
for k in sorted(set(joe_needs)):
    while i < len(can_sizes) and can_sizes[i] < k:
        i += 1

    dummy[k] = can_sizes[i] - k

answer = sum(dummy[k] for k in joe_needs)
