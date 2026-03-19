import heapq

INF = 10**18


def latest_ferry_departure(limit, d, cycle):
    if limit < d:
        return -1
    k = (limit - d) // cycle
    return d + k * cycle


def solve():
    import sys
    input = sys.stdin.readline

    T, J, R, F, jf, ji = map(int, input().split())

    graph = [[] for _ in range(J)]

    # roads
    for _ in range(R):
        a, b, t = map(int, input().split())
        graph[a].append(("road", b, t))
        graph[b].append(("road", a, t))

    # ferries
    for _ in range(F):
        j1, j2, d, tout, tin = map(int, input().split())
        cycle = tout + tin

        graph[j1].append(("ferry_out", j2, d, tout, cycle))
        graph[j2].append(("ferry_in", j1, d + tout, tin, cycle))

    latest = [-INF] * J
    latest[ji] = T

    pq = [(-T, ji)]

    while pq:
        t, u = heapq.heappop(pq)
        t = -t

        if t < latest[u]:
            continue

        for edge in graph[u]:

            if edge[0] == "road":
                _, v, cost = edge
                dep = t - cost

            else:
                _, v, d, travel, cycle = edge
                limit = t - travel
                dep = latest_ferry_departure(limit, d, cycle)

            if dep > latest[v]:
                latest[v] = dep
                heapq.heappush(pq, (-dep, v))

    print(max(0, latest[jf]))


if __name__ == "__main__":
    solve()


# CORRECT ANSWER

import sys
import heapq

input = sys.stdin.readline
INF = 10**18


def earliest_arrival(start_time, J, graph):
    dist = [INF] * J
    dist[start_time[0]] = start_time[1]

    pq = [(start_time[1], start_time[0])]

    while pq:
        time, u = heapq.heappop(pq)

        if time > dist[u]:
            continue

        for edge in graph[u]:

            if edge[0] == "road":
                _, v, t = edge
                new_time = time + t

            else:
                _, v, d, travel, cycle = edge

                if time <= d:
                    depart = d
                else:
                    k = (time - d + cycle - 1) // cycle
                    depart = d + k * cycle

                new_time = depart + travel

            if new_time < dist[v]:
                dist[v] = new_time
                heapq.heappush(pq, (new_time, v))

    return dist


def can_leave(L, jf, ji, T, J, graph):
    dist = earliest_arrival((jf, L), J, graph)
    return dist[ji] <= T


def solve():
    T, J, R, F, jf, ji = map(int, input().split())

    graph = [[] for _ in range(J)]

    # roads
    for _ in range(R):
        a, b, t = map(int, input().split())
        graph[a].append(("road", b, t))
        graph[b].append(("road", a, t))

    # ferries
    for _ in range(F):
        j1, j2, d, tout, tin = map(int, input().split())
        cycle = tout + tin

        graph[j1].append(("ferry", j2, d, tout, cycle))
        graph[j2].append(("ferry", j1, d + tout, tin, cycle))

    lo = 0
    hi = T
    ans = 0

    while lo <= hi:
        mid = (lo + hi) // 2

        if can_leave(mid, jf, ji, T, J, graph):
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1

    print(ans)


if __name__ == "__main__":
    solve()
