import sys


def cs(intervals, capacity, allow_weekends):
    max_day = max(e for _, e in intervals)
    used = [0] * (max_day + 1)

    for b, e in intervals:
        placed = False
        for d in range(b, e + 1):
            if not allow_weekends:
                # Skip Saturdays and Sundays
                if (d - 1) % 7 + 1 > 5:
                    continue
            if used[d] < capacity:
                used[d] += 1
                placed = True
                break
        if not placed:
            return False
    return True


def main():
    data = sys.stdin.read().split()
    idx = 0
    T = int(data[idx])
    idx += 1

    out = []

    for _ in range(T):
        m = int(data[idx])
        p = int(data[idx + 1])
        idx += 2

        intervals = []
        for _ in range(m):
            b = int(data[idx])
            e = int(data[idx + 1])
            idx += 2
            intervals.append((b, e))

        # Sort by earliest end day
        intervals.sort(key=lambda x: x[1])

        capacity = p // 2

        # Phase 1: weekdays only
        if cs(intervals, capacity, allow_weekends=False):
            out.append("fine")
        # Phase 2: all days
        elif cs(intervals, capacity, allow_weekends=True):
            out.append("weekend work")
        else:
            out.append("serious trouble")

    print("\n".join(out))


if __name__ == "__main__":
    main()
