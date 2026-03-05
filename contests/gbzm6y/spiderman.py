# https://open.kattis.com/problems/spiderman

def compute(n: int, a: list[int]) -> str:
    curr = {0: 0}

    parent = {}

    for i in range(n):
        nxt = {}

        for h, peak in curr.items():
            up = h + a[i]
            up_peak = max(peak, up)

            if up not in nxt or up_peak < nxt[up]:
                nxt[up] = up_peak
                parent[(i, up)] = (h, "U")

            down = h - a[i]
            if down >= 0:
                down_peak = peak

                if down not in nxt or down_peak < nxt[down]:
                    nxt[down] = down_peak
                    parent[(i, down)] = (h, "D")

        curr = nxt

    print(parent)

    # must end at height 0
    if 0 not in curr:
        return "IMPOSSIBLE"

    # -------- traceback --------
    res = []
    height = 0

    for i in reversed(range(n)):
        prev_h, move = parent[(i, height)]
        res.append(move)
        height = prev_h

    res.reverse()
    return "".join(res)


def __init__():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))

        print(compute(n, a))


__init__()
