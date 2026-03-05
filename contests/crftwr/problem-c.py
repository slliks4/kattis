def is_prime(n):
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False

    # step "2" ensures only odd numbers are checked
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_prime_divisors(n):
    divisors = set()
    upper_bound = int(n**0.5)

    for i in range(2, upper_bound + 1):
        if n % i == 0:
            if is_prime(i):
                divisors.add(i)

            other = n // i
            if is_prime(other):
                divisors.add(other)

    return sorted(divisors)


def checker(c,n):
    if c == n:
        return "W"
    elif c > n:
        return "T"
    else:
        return "L"


def flip(label):
    if label == "W": return "L"
    if label == "L": return "W"

    return "T"


def final_outcome(outcome):
    if "W" in outcome:
        return "W"
    if "T" in outcome:
        return "T"

    return "L"


def run_game(n, start):
    label = {}
    dag = {}

    prime_divisors = get_prime_divisors(n)
    dag[1] = prime_divisors

    def create_dag(pd, level):
        tmp = []

        if len(level) == 0:
            return

        for i in pd:
            for j in level:
                x = i * j
                dag.setdefault(j, []).append(x)

                if x < n and x not in tmp:
                    tmp.append(x)

        return create_dag(pd, tmp)

    create_dag(prime_divisors, prime_divisors)

    nodes = sorted(dag)

    for i in range(len(nodes)-1,-1, -1):
        curr = nodes[i]
        tmp = []

        for j in dag[curr]:
            if j in label:
                tmp.append(flip(label[j]))
            else:
                tmp.append(checker(j,n))

        label[curr] = final_outcome(tmp)

    if label[1] == "W":
        return start
    elif label[1] == "L":
        return "Bob" if start == "Alice" else "Alice"
    else:
        return "tie"

out = []

x = int(input())

for _ in range(x):
    n, start = input().split()
    out.append(run_game(int(n), start))

print("\n".join(out))
