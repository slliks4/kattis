n = int(input().strip())

pairs = {}

for _ in range(n):
    st, et = map(int, input().split())
    pairs.setdefault(et, []).append((st, et))

se = sorted(pairs)

count = 0
current_end = -1

for et in se:
    best = max(pairs[et], key=lambda x: x[0])
    st, _ = best

    if st >= current_end:
        current_end = et
        count += 1

print(count)
