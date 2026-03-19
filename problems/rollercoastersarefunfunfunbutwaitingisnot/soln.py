import sys
from itertools import permutations


def computeMaximizedFunPoint(ridesArr):
    n = len(ridesArr)

    def apply_wait(fun, minutes):
        for _ in range(minutes):
            fun -= int(0.05 * fun)  # floor(0.05 * current)
            if fun < 0:
                return -1
        return fun

    def apply_walk(fun, minutes):
        fun -= 8 * minutes
        return fun

    def simulate(order):
        fun = 100
        cp = -1

        for ride_idx in order:
            cl = 0 if cp == -1 else (cp + 1)
            target_loc = ride_idx + 1
            walk_mins = abs(target_loc - cl)

            fun = apply_walk(fun, walk_mins)
            if fun < 0:
                return -1

            wait = ridesArr[ride_idx][0]
            fun = apply_wait(fun, wait)
            if fun < 0:
                return -1

            fun += ridesArr[ride_idx][1]
            cp = ride_idx

        cl = cp + 1
        walk_back = cl
        fun = apply_walk(fun, walk_back)
        if fun < 0:
            return -1

        return fun

    best_fun = -1

    for perm in permutations(range(n)):
        result = simulate(perm)
        if result > best_fun:
            best_fun = result

    print(best_fun)
    return best_fun


def main():
    input_data = sys.stdin.read().split()
    noOfRides = int(input_data[0])
    rides = []
    idx = 1
    for i in range(noOfRides):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        rides.append((a, b))
        idx += 2
    computeMaximizedFunPoint(rides)


if __name__ == "__main__":
    main()
