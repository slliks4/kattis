# https://open.kattis.com/problems/intervalcover

import sys

SCALE = 10**6


def to_int(x: float) -> int:
    return int(round(x * SCALE))


def compute(intervals, a, b):
    # Goldilocks / degenerate target: cover a single point
    if a == b:
        for start, end, idx in intervals:
            if start <= a <= end:
                print(1)
                print(idx)
                return
        print("impossible")
        return

    out = []
    curr = a
    i = 0
    n = len(intervals)

    while curr < b:
        found = False
        best_end = curr   # RESET each phase
        best_idx = -1     # RESET each phase

        # consume all intervals that can start at/ curr
        while i < n and intervals[i][0] <= curr:
            end = intervals[i][1]
            if end > best_end:
                best_end = end
                best_idx = intervals[i][2]
                found = True
            i += 1

        if not found:
            print("impossible")
            return

        out.append(best_idx)
        curr = best_end

    print(len(out))
    print(" ".join(map(str, out)))


def main():
    data = sys.stdin.buffer.read().split()
    p = 0

    while p < len(data):
        # Each test case begins with A B, then n, then n lines ai bi
        A = float(data[p])
        B = float(data[p + 1])
        p += 2
        n = int(data[p])
        p += 1

        a = to_int(A)
        b = to_int(B)

        intervals = []
        for idx in range(n):
            ai = float(data[p])
            bi = float(data[p + 1])
            p += 2
            start = to_int(ai)
            end = to_int(bi)
            intervals.append((start, end, idx))

        intervals.sort(key=lambda t: t[0])  # sort by start
        compute(intervals, a, b)


if __name__ == "__main__":
    main()
