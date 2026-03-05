import sys

answer = []

for line in sys.stdin:
    n = line.rstrip('\n')

    if n == "#":
        break

    c = n.count('1')

    if n[-1] == 'e' and c % 2 == 0:
        answer.append(n[:-1] + '0')

    if n[-1] == 'e' and c % 2 != 0:
        answer.append(n[:-1] + '1')

    if n[-1] == 'o' and c % 2 == 0:
        answer.append(n[:-1] + '1')

    if n[-1] == 'o' and c % 2 != 0:
        answer.append(n[:-1] + '0')

for j in answer:
    print(j)
