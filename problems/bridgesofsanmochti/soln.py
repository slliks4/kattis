import sys


def solve():
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            return

        B, P = map(int, line.split())
        if B == 0 and P == 0:
            return

        B = abs(B)

        C = []
        T = []

        for _ in range(B):
            c, t = map(int, sys.stdin.readline().split())
            C.append(c)
            T.append(t)

        # queues before each bridge
        queue = [0] * (B)
        queue[0] = P

        busy = [False] * B
        remaining = [0] * B
        unit_size = [0] * B

        finished = 0
        time = 0

        while finished < P:

            # start crossings if possible
            for i in range(B):
                if not busy[i] and queue[i] > 0:
                    size = min(C[i], queue[i])
                    queue[i] -= size

                    busy[i] = True
                    unit_size[i] = size
                    remaining[i] = T[i]

            # find next event
            dt = min(remaining[i] for i in range(B) if busy[i])
            time += dt

            # advance time
            for i in range(B):
                if busy[i]:
                    remaining[i] -= dt

            # process finished crossings
            for i in range(B):
                if busy[i] and remaining[i] == 0:
                    busy[i] = False

                    if i == B - 1:
                        finished += unit_size[i]
                    else:
                        queue[i + 1] += unit_size[i]

        print(time)


if __name__ == "__main__":
    solve()
