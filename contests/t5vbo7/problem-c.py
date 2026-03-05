import heapq
import sys


def solve():
    data = sys.stdin.read().strip().split()
    N, T = map(int, data[:2])

    people = []
    idx = 2
    for _ in range(N):
        C = int(data[idx])
        D = int(data[idx + 1])
        idx += 2
        people.append((D, C))

    # Sort by deadline
    people.sort()

    heap = []

    for deadline, cash in people:
        heapq.heappush(heap, cash)
        # We can serve at most deadline + 1 people by this time
        if len(heap) > deadline + 1:
            heapq.heappop(heap)

    print(sum(heap))


if __name__ == "__main__":
    solve()
